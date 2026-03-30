# app/ui/loans_view.py
# Loans screen for staff/admin: list loans, create a new loan, and mark loans as returned.


import customtkinter as ctk  # Modern themed Tk widgets
from tkinter import messagebox  # Simple pop-up dialogs (info/warn/confirm)
from datetime import datetime, timedelta  # Date calculations (loan period, due dates)
from app.repositories.loans_repo import (
    list_loans, get_loans_stats, create_loan,
    return_loan, get_available_books, get_active_members
)  # DB/repository layer functions for loans
from app.ui.modern_table_styles import ModernTable, StatCard  # Reusable table + stat card UI components


class LoansView(ctk.CTkFrame):
    # Main loans page UI
    def __init__(self, master):
        super().__init__(master, fg_color="#f0f0f0")

        # Main container for padding and layout consistency
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Header section: page title + primary action button
        header = ctk.CTkFrame(container, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))

        title = ctk.CTkLabel(
            header,
            text="Loans",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#2b2b2b"
        )
        title.pack(side="left")

        # Opens CreateLoanDialog
        btn_new = ctk.CTkButton(
            header,
            text="+ New Loan",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#1a5f3d",
            hover_color="#236b49",
            height=38,
            corner_radius=8,
            command=self.show_add_dialog
        )
        btn_new.pack(side="right")

        # Top stats cards (total/active/overdue/returned)
        self.stats_frame = ctk.CTkFrame(container, fg_color="transparent")
        self.stats_frame.pack(fill="x", pady=(0, 20))
        self.stats_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Toolbar: search + filter + buttons
        toolbar = ctk.CTkFrame(container, corner_radius=12, fg_color="white")
        toolbar.pack(fill="x", pady=(0, 20))

        toolbar_content = ctk.CTkFrame(toolbar, fg_color="transparent")
        toolbar_content.pack(fill="x", padx=16, pady=16)
        toolbar_content.grid_columnconfigure(0, weight=1)

        # Text search across member name / book title
        self.search_entry = ctk.CTkEntry(
            toolbar_content,
            placeholder_text="🔍  Search by member name or book title...",
            height=38,
            font=ctk.CTkFont(size=13),
            corner_radius=8
        )
        self.search_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        self.search_entry.bind("<Return>", lambda e: self.load())  # Enter triggers search

        # Status filter: All / Borrowed / Returned / Overdue
        self.status_filter = ctk.CTkComboBox(
            toolbar_content,
            values=["All", "Borrowed", "Returned", "Overdue"],
            width=130,
            height=38,
            font=ctk.CTkFont(size=13),
            command=lambda _: self.load()  # Reload table when selection changes
        )
        self.status_filter.set("All")
        self.status_filter.grid(row=0, column=1, padx=(0, 10))

        # Explicit search button (same as pressing Enter)
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
        btn_search.grid(row=0, column=2, padx=(0, 10))

        # Reset UI state and re-fetch everything
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
        btn_refresh.grid(row=0, column=3)

        # Table section (list of loans)
        table_section = ctk.CTkFrame(container, fg_color="transparent")
        table_section.pack(fill="both", expand=True)

        # “Showing X loan(s)” message area
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

        # Table configuration (columns + widths)
        columns = ("id", "member", "book", "borrow_date", "due_date", "return_date", "status")
        column_configs = {
            "id": {"heading": "ID", "width": 70, "anchor": "center"},
            "member": {"heading": "Member", "width": 220, "anchor": "w"},
            "book": {"heading": "Book", "width": 280, "anchor": "w"},
            "borrow_date": {"heading": "Borrowed", "width": 120, "anchor": "center"},
            "due_date": {"heading": "Due Date", "width": 120, "anchor": "center"},
            "return_date": {"heading": "Returned", "width": 120, "anchor": "center"},
            "status": {"heading": "Status", "width": 120, "anchor": "center"}
        }

        self.table = ModernTable(table_section, columns, column_configs)
        self.table.pack(fill="both", expand=True, pady=(0, 16))

        # Actions row (currently: mark returned)
        actions = ctk.CTkFrame(table_section, fg_color="transparent")
        actions.pack(fill="x")

        btn_return = ctk.CTkButton(
            actions,
            text="Mark as Returned",
            width=160,
            height=36,
            font=ctk.CTkFont(size=13),
            fg_color="#16a34a",
            hover_color="#15803d",
            corner_radius=8,
            command=self.mark_returned
        )
        btn_return.pack(side="left")

        # Initial load
        self.load_stats()
        self.load()

    def load_stats(self):
        # Fetch summary stats from repository layer and rebuild cards
        stats = get_loans_stats()

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
            "Active",
            stats["borrowed"],
            "📖",
            "#2563eb"
        ).grid(row=0, column=1, sticky="ew", padx=(0, 10))

        StatCard(
            self.stats_frame,
            "Overdue",
            stats["overdue"],
            "⚠️",
            "#dc2626"
        ).grid(row=0, column=2, sticky="ew", padx=(0, 10))

        StatCard(
            self.stats_frame,
            "Returned",
            stats["returned"],
            "✅",
            "#16a34a"
        ).grid(row=0, column=3, sticky="ew")

    def refresh(self):
        # Reset inputs back to default, then reload stats and table
        self.search_entry.delete(0, "end")
        self.status_filter.set("All")
        self.load_stats()
        self.load()

    def load(self):
        # Read UI filters and request matching loan records
        keyword = self.search_entry.get().strip()
        status_filter = self.status_filter.get().lower()
        if status_filter == "all":
            status_filter = ""

        self.table.clear()

        rows = list_loans(keyword, status_filter)

        if not rows:
            self.info.configure(text="No results found.")
            return

        self.info.configure(text=f"Showing {len(rows)} loan(s)")

        for r in rows:
            # Add colored tags for table styling (see ModernTable tag config)
            status = r[6]
            status_tags = []
            if status == "overdue":
                status_tags.append("overdue")
            elif status == "borrowed":
                status_tags.append("borrowed")
            elif status == "returned":
                status_tags.append("returned")

            self.table.insert_row(r, tags=status_tags)

    def show_add_dialog(self):
        # Opens the “Create new loan” modal window
        CreateLoanDialog(self, self.after_save)

    def mark_returned(self):
        # Marks the selected loan as returned (updates DB)
        loan_data = self.table.get_selected_values()
        if not loan_data:
            messagebox.showwarning("No Selection", "Please select a loan to mark as returned.")
            return

        loan_id = loan_data[0]
        status = loan_data[6]

        if status == "returned":
            messagebox.showinfo("Info", "This loan is already marked as returned.")
            return

        if messagebox.askyesno("Confirm Return", "Mark this loan as returned?"):
            if return_loan(loan_id):
                messagebox.showinfo("Success", "Loan marked as returned!")
                self.after_save()
            else:
                messagebox.showerror("Error", "Failed to mark loan as returned.")

    def after_save(self):
        # Standard callback to refresh UI after any changes
        self.load_stats()
        self.load()


class CreateLoanDialog(ctk.CTkToplevel):
    # Modal dialog to create a new loan record
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.callback = callback

        self.title("Create New Loan")
        self.geometry("500x450")
        self.resizable(False, False)
        self.transient(parent)  # keep on top of parent
        self.grab_set()  # modal behavior (block interactions with parent)

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=24, pady=24)

        title = ctk.CTkLabel(
            container,
            text="Create New Loan",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title.pack(pady=(0, 20))

        # Load dropdown data from repository
        members = get_active_members()
        books = get_available_books()

        # Early exits if there is nothing to select
        if not members:
            messagebox.showerror("Error", "No active members available!")
            self.destroy()
            return

        if not books:
            messagebox.showerror("Error", "No available books!")
            self.destroy()
            return

        self.member_combo = self._create_combo(container, "Member:", members)
        self.book_combo = self._create_combo(container, "Book:", books)

        # Loan period input (days)
        frame = ctk.CTkFrame(container, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 12))

        label = ctk.CTkLabel(frame, text="Loan Period (days):", font=ctk.CTkFont(size=13))
        label.pack(anchor="w", pady=(0, 4))

        self.days_entry = ctk.CTkEntry(frame, height=36)
        self.days_entry.insert(0, "14")  # Default loan period
        self.days_entry.pack(fill="x")

        # Helpful hint for the user
        info = ctk.CTkLabel(
            container,
            text="💡 Default loan period is 14 days",
            font=ctk.CTkFont(size=11),
            text_color="#666666"
        )
        info.pack(pady=(10, 20))

        # Buttons row
        btn_frame = ctk.CTkFrame(container, fg_color="transparent")
        btn_frame.pack(fill="x")

        btn_cancel = ctk.CTkButton(
            btn_frame,
            text="Cancel",
            width=120,
            height=38,
            fg_color="#6b7280",
            hover_color="#4b5563",
            command=self.destroy
        )
        btn_cancel.pack(side="right", padx=(10, 0))

        btn_save = ctk.CTkButton(
            btn_frame,
            text="Create Loan",
            width=120,
            height=38,
            fg_color="#1a5f3d",
            hover_color="#236b49",
            command=self.save
        )
        btn_save.pack(side="right")

    def _create_combo(self, parent, label_text, values):
        # Helper: label + combobox pair
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 12))

        label = ctk.CTkLabel(frame, text=label_text, font=ctk.CTkFont(size=13))
        label.pack(anchor="w", pady=(0, 4))

        combo = ctk.CTkComboBox(frame, height=36, values=values)
        if values:
            combo.set(values[0])
        combo.pack(fill="x")
        return combo

    def save(self):
        # Validate loan period input
        try:
            days = int(self.days_entry.get().strip())
            if days <= 0:
                raise ValueError()
        except:
            messagebox.showwarning("Validation", "Please enter a valid number of days!")
            return

        member = self.member_combo.get()
        book = self.book_combo.get()

        # Extract IDs from selection strings (expected format: "... (ID: X)")
        try:
            member_id = int(member.split("ID: ")[1].rstrip(")"))
            book_id = int(book.split("ID: ")[1].rstrip(")"))
        except:
            messagebox.showerror("Error", "Invalid selection format!")
            return

        data = {
            "member_id": member_id,
            "book_id": book_id,
            "days": days
        }

        # Persist to DB via repository
        result = create_loan(data)
        if result["success"]:
            messagebox.showinfo("Success", result["message"])
            self.callback()
            self.destroy()
        else:
            messagebox.showerror("Error", result["message"])
