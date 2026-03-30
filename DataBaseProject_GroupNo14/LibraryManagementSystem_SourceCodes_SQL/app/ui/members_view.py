# app/ui/members_view.py
# Members management screen for staff/admin: list members, create new member, edit and delete.


import customtkinter as ctk  # Modern themed Tk widgets
from tkinter import messagebox  # Pop-up dialogs for validation/errors/confirmations
from app.repositories.members_repo import (
    list_members, get_members_stats, add_member,
    update_member, delete_member
)  # Repository/database layer functions
from app.ui.modern_table_styles import ModernTable, StatCard  # Reusable table + stat cards


class MembersView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#f0f0f0")

        # Main container for consistent padding
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Header: title + “New Member”
        header = ctk.CTkFrame(container, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))

        title = ctk.CTkLabel(
            header,
            text="Members",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#2b2b2b"
        )
        title.pack(side="left")

        btn_new = ctk.CTkButton(
            header,
            text="+ New Member",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#1a5f3d",
            hover_color="#236b49",
            height=38,
            corner_radius=8,
            command=self.show_add_dialog
        )
        btn_new.pack(side="right")

        # Top stats cards
        self.stats_frame = ctk.CTkFrame(container, fg_color="transparent")
        self.stats_frame.pack(fill="x", pady=(0, 20))
        self.stats_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Toolbar: search + buttons
        toolbar = ctk.CTkFrame(container, corner_radius=12, fg_color="white")
        toolbar.pack(fill="x", pady=(0, 20))

        toolbar_content = ctk.CTkFrame(toolbar, fg_color="transparent")
        toolbar_content.pack(fill="x", padx=16, pady=16)
        toolbar_content.grid_columnconfigure(0, weight=1)

        self.search_entry = ctk.CTkEntry(
            toolbar_content,
            placeholder_text="🔍  Search by name or email...",
            height=38,
            font=ctk.CTkFont(size=13),
            corner_radius=8
        )
        self.search_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        self.search_entry.bind("<Return>", lambda e: self.load())  # Enter triggers search

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

        # Table: member rows
        columns = ("id", "name", "phone", "email", "permission")
        column_configs = {
            "id": {"heading": "ID", "width": 70, "anchor": "center"},
            "name": {"heading": "Full Name", "width": 280, "anchor": "w"},
            "phone": {"heading": "Phone", "width": 170, "anchor": "w"},
            "email": {"heading": "Email", "width": 320, "anchor": "w"},
            "permission": {"heading": "Role", "width": 140, "anchor": "center"}
        }

        self.table = ModernTable(table_section, columns, column_configs)
        self.table.pack(fill="both", expand=True, pady=(0, 16))

        # Actions row
        actions = ctk.CTkFrame(table_section, fg_color="transparent")
        actions.pack(fill="x")

        btn_edit = ctk.CTkButton(
            actions,
            text="Edit",
            width=110,
            height=36,
            font=ctk.CTkFont(size=13),
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            corner_radius=8,
            command=self.show_edit_dialog
        )
        btn_edit.pack(side="left", padx=(0, 10))

        btn_delete = ctk.CTkButton(
            actions,
            text="Delete",
            width=110,
            height=36,
            font=ctk.CTkFont(size=13),
            fg_color="#dc2626",
            hover_color="#b91c1c",
            corner_radius=8,
            command=self.delete_selected
        )
        btn_delete.pack(side="left")

        # Initial load
        self.load_stats()
        self.load()

    def load_stats(self):
        # Fetch member summary stats and rebuild stat cards
        stats = get_members_stats()

        for widget in self.stats_frame.winfo_children():
            widget.destroy()

        StatCard(
            self.stats_frame,
            "Total Members",
            stats["total"],
            "👥",
            "#1a5f3d"
        ).grid(row=0, column=0, sticky="ew", padx=(0, 10))

        StatCard(
            self.stats_frame,
            "Active Borrowers",
            stats["active"],
            "📖",
            "#2563eb"
        ).grid(row=0, column=1, sticky="ew", padx=(0, 10))

        StatCard(
            self.stats_frame,
            "New This Month",
            stats["new_this_month"],
            "✨",
            "#16a34a"
        ).grid(row=0, column=2, sticky="ew")

    def refresh(self):
        # Reset search and reload the view
        self.search_entry.delete(0, "end")
        self.load_stats()
        self.load()

    def load(self):
        # Load members matching the keyword
        keyword = self.search_entry.get().strip()
        self.table.clear()

        rows = list_members(keyword)

        if not rows:
            self.info.configure(text="No results found.")
            return

        self.info.configure(text=f"Showing {len(rows)} member(s)")

        for r in rows:
            self.table.insert_row(r)

    def show_add_dialog(self):
        # Open add member dialog
        AddMemberDialog(self, self.after_save)

    def show_edit_dialog(self):
        # Open edit dialog for selected member
        member_data = self.table.get_selected_values()
        if not member_data:
            messagebox.showwarning("No Selection", "Please select a member to edit.")
            return
        EditMemberDialog(self, member_data, self.after_save)

    def delete_selected(self):
        # Delete selected member after confirmation
        member_data = self.table.get_selected_values()
        if not member_data:
            messagebox.showwarning("No Selection", "Please select a member to delete.")
            return

        member_id = member_data[0]
        name = member_data[1]

        if messagebox.askyesno("Confirm Delete", f"Delete member '{name}'?"):
            if delete_member(member_id):
                messagebox.showinfo("Success", "Member deleted successfully!")
                self.after_save()
            else:
                messagebox.showerror("Error", "Failed to delete member.")

    def after_save(self):
        # Standard callback to refresh UI after a DB update
        self.load_stats()
        self.load()


class AddMemberDialog(ctk.CTkToplevel):
    # Modal dialog: create a new member record
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.callback = callback

        self.title("Add New Member")
        self.geometry("500x650")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=24, pady=24)

        title = ctk.CTkLabel(
            container,
            text="Add New Member",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title.pack(pady=(0, 20))

        # Input fields
        self.first_name_entry = self._create_field(container, "First Name:")
        self.last_name_entry = self._create_field(container, "Last Name:")
        self.phone_entry = self._create_field(container, "Phone:")
        self.email_entry = self._create_field(container, "Email:")
        self.password_entry = self._create_field(container, "Password:")
        self.permission_combo = self._create_combo(
            container, "Role:", ["member", "librarian", "admin"]
        )

        # Buttons row
        btn_frame = ctk.CTkFrame(container, fg_color="transparent")
        btn_frame.pack(fill="x", pady=(20, 0))

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
            text="Save Member",
            width=120,
            height=38,
            fg_color="#1a5f3d",
            hover_color="#236b49",
            command=self.save
        )
        btn_save.pack(side="right")

    def _create_field(self, parent, label_text):
        # Helper: label + entry pair
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 12))

        label = ctk.CTkLabel(frame, text=label_text, font=ctk.CTkFont(size=13))
        label.pack(anchor="w", pady=(0, 4))

        entry = ctk.CTkEntry(frame, height=36)
        entry.pack(fill="x")
        return entry

    def _create_combo(self, parent, label_text, values):
        # Helper: label + combobox pair
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 12))

        label = ctk.CTkLabel(frame, text=label_text, font=ctk.CTkFont(size=13))
        label.pack(anchor="w", pady=(0, 4))

        combo = ctk.CTkComboBox(frame, height=36, values=values)
        combo.set(values[0])
        combo.pack(fill="x")
        return combo

    def save(self):
        # Validate required fields
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not all([first_name, last_name, email, password]):
            messagebox.showwarning("Validation", "All fields except phone are required!")
            return

        data = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": self.phone_entry.get().strip(),
            "email": email,
            "password": password,
            "permission": self.permission_combo.get()
        }

        # Persist to DB
        if add_member(data):
            messagebox.showinfo("Success", "Member added successfully!")
            self.callback()
            self.destroy()
        else:
            messagebox.showerror("Error", "Failed to add member. Email may already exist.")


class EditMemberDialog(ctk.CTkToplevel):
    # Modal dialog: update an existing member
    def __init__(self, parent, member_data, callback):
        super().__init__(parent)
        self.member_id = member_data[0]
        self.callback = callback

        self.title("Edit Member")
        self.geometry("500x550")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=24, pady=24)

        title = ctk.CTkLabel(
            container,
            text="Edit Member",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title.pack(pady=(0, 20))

        # Split the “Full Name” column into first/last name for editing
        full_name = member_data[1]
        names = full_name.split(" ", 1)
        first_name = names[0] if len(names) > 0 else ""
        last_name = names[1] if len(names) > 1 else ""

        self.first_name_entry = self._create_field(container, "First Name:")
        self.first_name_entry.insert(0, first_name)

        self.last_name_entry = self._create_field(container, "Last Name:")
        self.last_name_entry.insert(0, last_name)

        self.phone_entry = self._create_field(container, "Phone:")
        self.phone_entry.insert(0, member_data[2] or "")

        self.email_entry = self._create_field(container, "Email:")
        self.email_entry.insert(0, member_data[3])

        # Optional password update (blank = keep current password)
        self.password_entry = self._create_field(container, "New Password (leave blank to keep current):")

        self.permission_combo = self._create_combo(
            container, "Role:", ["member", "librarian", "admin"]
        )
        self.permission_combo.set(member_data[4])

        # Buttons row
        btn_frame = ctk.CTkFrame(container, fg_color="transparent")
        btn_frame.pack(fill="x", pady=(20, 0))

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
            text="Update Member",
            width=120,
            height=38,
            fg_color="#1a5f3d",
            hover_color="#236b49",
            command=self.save
        )
        btn_save.pack(side="right")

    def _create_field(self, parent, label_text):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 12))

        label = ctk.CTkLabel(frame, text=label_text, font=ctk.CTkFont(size=13))
        label.pack(anchor="w", pady=(0, 4))

        entry = ctk.CTkEntry(frame, height=36)
        entry.pack(fill="x")
        return entry

    def _create_combo(self, parent, label_text, values):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 12))

        label = ctk.CTkLabel(frame, text=label_text, font=ctk.CTkFont(size=13))
        label.pack(anchor="w", pady=(0, 4))

        combo = ctk.CTkComboBox(frame, height=36, values=values)
        combo.pack(fill="x")
        return combo

    def save(self):
        # Validate required fields
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        email = self.email_entry.get().strip()

        if not all([first_name, last_name, email]):
            messagebox.showwarning("Validation", "First name, last name, and email are required!")
            return

        data = {
            "member_id": self.member_id,
            "first_name": first_name,
            "last_name": last_name,
            "phone": self.phone_entry.get().strip(),
            "email": email,
            "password": self.password_entry.get().strip(),
            "permission": self.permission_combo.get()
        }

        # Persist update to DB
        if update_member(data):
            messagebox.showinfo("Success", "Member updated successfully!")
            self.callback()
            self.destroy()
        else:
            messagebox.showerror("Error", "Failed to update member.")
