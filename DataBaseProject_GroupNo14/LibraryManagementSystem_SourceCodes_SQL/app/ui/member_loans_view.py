# app/ui/member_loans_view.py
# Member-facing loans screen: shows only the logged-in member's loan history and stats.


import customtkinter as ctk  # Modern themed Tk widgets
from app.repositories.member_loans_repo import get_member_loans, get_member_loan_stats  # Member-only loan queries
from app.ui.modern_table_styles import ModernTable, StatCard  # Reusable UI components


class MemberLoansView(ctk.CTkFrame):
    def __init__(self, master, user_data):
        super().__init__(master, fg_color="#f0f0f0")
        self.user_data = user_data
        self.member_id = user_data.get('id')  # Member identifier for DB queries

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Header
        header = ctk.CTkFrame(container, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))

        title = ctk.CTkLabel(
            header,
            text="My Loans",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#2b2b2b"
        )
        title.pack(side="left")

        # Stats cards
        self.stats_frame = ctk.CTkFrame(container, fg_color="transparent")
        self.stats_frame.pack(fill="x", pady=(0, 20))
        self.stats_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Info banner (reminder about due dates)
        info_banner = ctk.CTkFrame(container, corner_radius=12, fg_color="#fef3c7")
        info_banner.pack(fill="x", pady=(0, 20))

        info_content = ctk.CTkFrame(info_banner, fg_color="transparent")
        info_content.pack(fill="x", padx=20, pady=12)

        info_icon = ctk.CTkLabel(
            info_content,
            text="💡",
            font=ctk.CTkFont(size=18),
            text_color="#92400e"
        )
        info_icon.pack(side="left", padx=(0, 12))

        info_text = ctk.CTkLabel(
            info_content,
            text="View your borrowed books and their due dates. Please return books on time to avoid penalties.",
            font=ctk.CTkFont(size=12),
            text_color="#92400e"
        )
        info_text.pack(side="left")

        # Toolbar (only refresh, since member view is simpler)
        toolbar = ctk.CTkFrame(container, corner_radius=12, fg_color="white")
        toolbar.pack(fill="x", pady=(0, 20))

        toolbar_content = ctk.CTkFrame(toolbar, fg_color="transparent")
        toolbar_content.pack(fill="x", padx=16, pady=16)

        btn_refresh = ctk.CTkButton(
            toolbar_content,
            text="🔄  Refresh",
            width=120,
            height=38,
            font=ctk.CTkFont(size=13),
            fg_color="#1a5f3d",
            hover_color="#236b49",
            corner_radius=8,
            command=self.refresh
        )
        btn_refresh.pack(side="right")

        # Table section
        table_section = ctk.CTkFrame(container, fg_color="transparent")
        table_section.pack(fill="both", expand=True)

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

        # Table: member loan records
        columns = ("loan_id", "book_title", "borrow_date", "due_date", "return_date", "status")
        column_configs = {
            "loan_id": {"heading": "Loan ID", "width": 90, "anchor": "center"},
            "book_title": {"heading": "Book Title", "width": 400, "anchor": "w"},
            "borrow_date": {"heading": "Borrowed", "width": 130, "anchor": "center"},
            "due_date": {"heading": "Due Date", "width": 130, "anchor": "center"},
            "return_date": {"heading": "Returned", "width": 130, "anchor": "center"},
            "status": {"heading": "Status", "width": 120, "anchor": "center"}
        }

        self.table = ModernTable(table_section, columns, column_configs)
        self.table.pack(fill="both", expand=True)

        self.load_stats()
        self.load()

    def load_stats(self):
        # If we do not have an ID, we cannot query member-specific stats
        if not self.member_id:
            return

        stats = get_member_loan_stats(self.member_id)

        for widget in self.stats_frame.winfo_children():
            widget.destroy()

        StatCard(
            self.stats_frame,
            "Total Loans",
            stats["total"],
            "📋",
            "#1a5f3d"
        ).grid(row=0, column=0, sticky="ew", padx=(0, 10))

        StatCard(
            self.stats_frame,
            "Currently Borrowed",
            stats["active"],
            "📖",
            "#2563eb"
        ).grid(row=0, column=1, sticky="ew", padx=(0, 10))

        StatCard(
            self.stats_frame,
            "Overdue Books",
            stats["overdue"],
            "⚠️",
            "#dc2626" if stats["overdue"] > 0 else "#16a34a"
        ).grid(row=0, column=2, sticky="ew")

    def refresh(self):
        # Refresh stats and table
        self.load_stats()
        self.load()

    def load(self):
        # Load only this member's loans
        if not self.member_id:
            self.info.configure(text="User information not available.")
            return

        self.table.clear()

        rows = get_member_loans(self.member_id)

        if not rows:
            self.info.configure(text="You have no loan records.")
            return

        self.info.configure(text=f"Showing {len(rows)} loan(s)")

        for r in rows:
            # Add tags for color styling
            status = r[5]
            status_tags = []
            if status == "overdue":
                status_tags.append("overdue")
            elif status == "borrowed":
                status_tags.append("borrowed")
            elif status == "returned":
                status_tags.append("returned")

            self.table.insert_row(r, tags=status_tags)
