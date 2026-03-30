# app/ui/overdue_view.py

import customtkinter as ctk  # Modern UI widgets (frames, buttons, labels, etc.)
from tkinter import messagebox  # Classic Tk message dialogs (yes/no, warning, info)
from app.repositories.overdue_repo import list_overdue_loans, mark_loans_overdue  # DB-facing functions
from app.ui.modern_table_styles import ModernTable, StatCard  # Reusable table + stats UI components


class OverdueView(ctk.CTkFrame):
    def __init__(self, master):
        # This view shows loans that are past due date, grouped by severity (days overdue)
        super().__init__(master, fg_color="#f0f0f0")

        # Main page container (adds padding around content)
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Header row (title + action button)
        header = ctk.CTkFrame(container, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))

        title = ctk.CTkLabel(
            header,
            text="Overdue Loans",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#2b2b2b"
        )
        title.pack(side="left")

        # Updates DB-side overdue statuses (e.g., mark borrowed -> overdue if due_date passed)
        btn_update = ctk.CTkButton(
            header,
            text="🔄  Update Overdue Status",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#ea580c",
            hover_color="#c2410c",
            height=38,
            corner_radius=8,
            command=self.update_overdue_status
        )
        btn_update.pack(side="right")

        # Stats cards (summary at a glance)
        self.stats_frame = ctk.CTkFrame(container, fg_color="transparent")
        self.stats_frame.pack(fill="x", pady=(0, 20))
        self.stats_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Alert banner (static explanation / guidance)
        alert = ctk.CTkFrame(container, corner_radius=12, fg_color="#fef3c7")
        alert.pack(fill="x", pady=(0, 20))

        alert_content = ctk.CTkFrame(alert, fg_color="transparent")
        alert_content.pack(fill="x", padx=20, pady=16)

        alert_icon = ctk.CTkLabel(
            alert_content,
            text="⚠️",
            font=ctk.CTkFont(size=20),
            text_color="#92400e"
        )
        alert_icon.pack(side="left", padx=(0, 12))

        alert_text = ctk.CTkLabel(
            alert_content,
            text="These loans are past their due date. Please contact the members for book returns.",
            font=ctk.CTkFont(size=13),
            text_color="#92400e",
            wraplength=900,
            justify="left"
        )
        alert_text.pack(side="left", fill="x", expand=True)

        # Toolbar (search + refresh)
        toolbar = ctk.CTkFrame(container, corner_radius=12, fg_color="white")
        toolbar.pack(fill="x", pady=(0, 20))

        toolbar_content = ctk.CTkFrame(toolbar, fg_color="transparent")
        toolbar_content.pack(fill="x", padx=16, pady=16)
        toolbar_content.grid_columnconfigure(0, weight=1)

        # Search is limited to member name (as implemented in repo query)
        self.search_entry = ctk.CTkEntry(
            toolbar_content,
            placeholder_text="🔍  Search by member name...",
            height=38,
            font=ctk.CTkFont(size=13),
            corner_radius=8
        )
        self.search_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        self.search_entry.bind("<Return>", lambda e: self.load())  # Enter triggers load()

        btn_search = ctk.CTkButton(
            toolbar_content,
            text="Search",
            width=100,
            height=38,
            font=ctk.CTkFont(size=13),
            fg_color="#1a5f3d",
            hover_color="#236b49",
            corner_radius=8,
            command=self.load
        )
        btn_search.grid(row=0, column=1, padx=(0, 10))

        btn_refresh = ctk.CTkButton(
            toolbar_content,
            text="🔄  Refresh",
            width=100,
            height=38,
            font=ctk.CTkFont(size=13),
            fg_color="#505050",
            hover_color="#606060",
            corner_radius=8,
            command=self.refresh
        )
        btn_refresh.grid(row=0, column=2)

        # Table section
        table_section = ctk.CTkFrame(container, fg_color="transparent")
        table_section.pack(fill="both", expand=True)

        # Small info label above the table ("showing X ...")
        info_frame = ctk.CTkFrame(table_section, fg_color="transparent")
        info_frame.pack(fill="x", pady=(0, 12))

        self.info = ctk.CTkLabel(
            info_frame,
            text="",
            font=ctk.CTkFont(size=12),
            text_color="#666666",
            anchor="w"
        )
        self.info.pack(side="left")

        # Table columns (match what overdue_repo.list_overdue_loans returns)
        columns = ("loan_id", "member", "email", "book", "due_date", "days_overdue")
        column_configs = {
            "loan_id": {"heading": "Loan ID", "width": 90, "anchor": "center"},
            "member": {"heading": "Member", "width": 220, "anchor": "w"},
            "email": {"heading": "Email", "width": 280, "anchor": "w"},
            "book": {"heading": "Book", "width": 300, "anchor": "w"},
            "due_date": {"heading": "Due Date", "width": 120, "anchor": "center"},
            "days_overdue": {"heading": "Days Overdue", "width": 140, "anchor": "center"}
        }

        self.table = ModernTable(table_section, columns, column_configs)
        self.table.pack(fill="both", expand=True)

        # Initial load (stats first, then table data)
        self.load_stats()
        self.load()

    def load_stats(self):
        # We reuse the same repo function with empty keyword to get ALL overdue rows
        rows = list_overdue_loans("")
        total = len(rows)

        # Severity buckets (simple business rule for UI highlighting)
        critical = sum(1 for r in rows if r[5] > 30)         # More than 30 days
        moderate = sum(1 for r in rows if 7 < r[5] <= 30)    # 7-30 days
        recent = sum(1 for r in rows if r[5] <= 7)           # Up to 7 days

        # Clear existing cards before re-drawing
        for widget in self.stats_frame.winfo_children():
            widget.destroy()

        StatCard(
            self.stats_frame,
            "Total Overdue",
            total,
            "⏰",
            "#dc2626"
        ).grid(row=0, column=0, sticky="ew", padx=(0, 10))

        StatCard(
            self.stats_frame,
            "Critical (30+ days)",
            critical,
            "🚨",
            "#991b1b"
        ).grid(row=0, column=1, sticky="ew", padx=(0, 10))

        StatCard(
            self.stats_frame,
            "Moderate (7-30 days)",
            moderate,
            "⚠️",
            "#ea580c"
        ).grid(row=0, column=2, sticky="ew")

    def refresh(self):
        # Reset search and reload everything from DB
        self.search_entry.delete(0, "end")
        self.load_stats()
        self.load()

    def load(self):
        keyword = self.search_entry.get().strip()
        self.table.clear()

        # Repo returns rows with (loan_id, member, email, book, due_date, days_overdue)
        rows = list_overdue_loans(keyword)

        if not rows:
            self.info.configure(text="No overdue loans found. Great!")
            return

        self.info.configure(text=f"⚠️  {len(rows)} overdue loan(s) requiring attention")

        for r in rows:
            # Color code each row by severity using ModernTable tags
            days_overdue = r[5]
            severity_tags = []
            if days_overdue > 30:
                severity_tags.append("critical")
            elif days_overdue > 7:
                severity_tags.append("moderate")
            else:
                severity_tags.append("recent")

            self.table.insert_row(r, tags=severity_tags)

    def update_overdue_status(self):
        # Confirmation dialog because this action affects multiple DB records
        if messagebox.askyesno(
                "Update Overdue Status",
                "This will update the status of all loans that are past their due date. Continue?"
        ):
            # Repo function performs the DB update (e.g., borrowed -> overdue where due_date < today)
            if mark_loans_overdue():
                messagebox.showinfo("Success", "Overdue status updated successfully!")
                self.refresh()
            else:
                messagebox.showerror("Error", "Failed to update overdue status.")
