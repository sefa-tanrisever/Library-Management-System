# app/ui/books_view.py
# UI view for Books: builds widgets (tables, forms, buttons) and calls repository functions to show/update data.

import customtkinter as ctk
# Tkinter messagebox is used for simple pop-up dialogs (info / warning / confirm).
from tkinter import messagebox
# Repository functions (database queries) used by this UI screen.
from app.repositories.books_repo import (
    list_books, get_books_stats, add_book,
    update_book, delete_book, get_authors, get_sections, get_publishers,
    get_languages
)
# Other UI pages/components that are loaded into the main window.
from app.ui.modern_table_styles import ModernTable, StatCard


# Main class: BooksView (defined in books_view.py).
class BooksView(ctk.CTkFrame):
    # Build the UI for this window/frame and wire up callbacks.
    def __init__(self, master):
        super().__init__(master, fg_color="#f0f0f0")
        self.pack_propagate(False)

        # Main container
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Header
        header = ctk.CTkFrame(container, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))

        title = ctk.CTkLabel(
            header,
            text="Books",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#2b2b2b"
        )
        title.pack(side="left")

        btn_new = ctk.CTkButton(
            header,
            text="+ New Book",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#1a5f3d",
            hover_color="#236b49",
            height=38,
            corner_radius=8,
            command=self.show_add_dialog
        )
        btn_new.pack(side="right")

        # Stats cards
        self.stats_frame = ctk.CTkFrame(container, fg_color="transparent")
        self.stats_frame.pack(fill="x", pady=(0, 20))
        self.stats_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Toolbar
        toolbar = ctk.CTkFrame(container, corner_radius=12, fg_color="white")
        toolbar.pack(fill="x", pady=(0, 20))

        toolbar_content = ctk.CTkFrame(toolbar, fg_color="transparent")
        toolbar_content.pack(fill="x", padx=16, pady=16)
        toolbar_content.grid_columnconfigure(0, weight=1)

        self.search_entry = ctk.CTkEntry(
            toolbar_content,
            placeholder_text="🔍  Search by title...",
            height=38,
            font=ctk.CTkFont(size=13),
            corner_radius=8
        )
        self.search_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        self.search_entry.bind("<Return>", lambda e: self.load())

        # Language filter
        self.language_filter = ctk.CTkComboBox(
            toolbar_content,
            values=["All Languages"] + get_languages(),
            width=150,
            height=38,
            font=ctk.CTkFont(size=13),
            command=lambda _: self.load()
        )
        self.language_filter.set("All Languages")
        self.language_filter.grid(row=0, column=1, padx=(0, 10))

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

        # Table section
        table_section = ctk.CTkFrame(container, fg_color="transparent")
        table_section.pack(fill="both", expand=True)

        # Info label
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

        # Modern table
        columns = ("id", "title", "author", "section", "publisher", "language", "status")
        column_configs = {
            "id": {"heading": "ID", "width": 70, "anchor": "center"},
            "title": {"heading": "Title", "width": 320, "anchor": "w"},
            "author": {"heading": "Author", "width": 200, "anchor": "w"},
            "section": {"heading": "Section", "width": 160, "anchor": "w"},
            "publisher": {"heading": "Publisher", "width": 180, "anchor": "w"},
            "language": {"heading": "Language", "width": 160,"anchor":"w"},
            "status": {"heading": "Status", "width": 130, "anchor": "center"}
        }

        self.table = ModernTable(table_section, columns, column_configs)
        self.table.pack(fill="both", expand=True, pady=(0, 16))

        # Action buttons
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

        self.load_stats()
        self.load()

    # Load summary/statistics data for the top dashboard cards.
    def load_stats(self):
        stats = get_books_stats()

        # Clear existing cards
        for widget in self.stats_frame.winfo_children():
            widget.destroy()

        StatCard(
            self.stats_frame,
            "Total Books",
            stats["total"],
            "📚",
            "#1a5f3d"
        ).grid(row=0, column=0, sticky="ew", padx=(0, 10))

        StatCard(
            self.stats_frame,
            "Available",
            stats["available"],
            "✅",
            "#16a34a"
        ).grid(row=0, column=1, sticky="ew", padx=(0, 10))

        StatCard(
            self.stats_frame,
            "Borrowed",
            stats["borrowed"],
            "📖",
            "#2563eb"
        ).grid(row=0, column=2, sticky="ew", padx=(0, 10))

        StatCard(
            self.stats_frame,
            "Maintenance",
            stats["maintenance"],
            "🔧",
            "#ea580c"
        ).grid(row=0, column=3, sticky="ew")

    # Reset filters/search fields and reload the view.
    def refresh(self):
        self.search_entry.delete(0, "end")
        self.language_filter.set("All Languages")
        self.load_stats()
        self.load()

    # Fetch the latest rows from the database and refresh the table.
    def load(self):
        keyword = self.search_entry.get().strip()
        language = self.language_filter.get()
        if language == "All Languages":
            language = ""

        self.table.clear()

        rows = list_books(keyword, language)

        if not rows:
            self.info.configure(text="No results found.")
            return

        self.info.configure(text=f"Showing {len(rows)} book(s)")

        for r in rows:
            # Determine status tag
            status = r[6]
            status_tags = []
            if status == "available":
                status_tags.append("available")
            elif status == "borrowed":
                status_tags.append("borrowed")

            self.table.insert_row(r, tags=status_tags)

    # Open the corresponding dialog/window for this action.
    def show_add_dialog(self):
        AddBookDialog(self, self.after_save)

    # Open the corresponding dialog/window for this action.
    def show_edit_dialog(self):
        book_data = self.table.get_selected_values()
        if not book_data:
            messagebox.showwarning("No Selection", "Please select a book to edit.")
            return
        EditBookDialog(self, book_data, self.after_save)

    # Delete the currently selected record after confirmation.
    def delete_selected(self):
        book_data = self.table.get_selected_values()
        if not book_data:
            messagebox.showwarning("No Selection", "Please select a book to delete.")
            return

        book_id = book_data[0]
        title = book_data[1]

        if messagebox.askyesno("Confirm Delete", f"Delete '{title}'?"):
            if delete_book(book_id):
                messagebox.showinfo("Success", "Book deleted successfully!")
                self.after_save()
            else:
                messagebox.showerror("Error", "Failed to delete book.")

    # Callback used after a successful save to refresh the current screen.
    def after_save(self):
        self.load_stats()
        self.load()


# Main class: AddBookDialog (defined in books_view.py).
class AddBookDialog(ctk.CTkToplevel):
    # Build the UI for this window/frame and wire up callbacks.
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.callback = callback

        self.title("Add New Book")
        self.geometry("500x650")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=24, pady=24)

        title = ctk.CTkLabel(
            container,
            text="Add New Book",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title.pack(pady=(0, 20))

        self.title_entry = self._create_field(container, "Title:")
        self.author_combo = self._create_combo(container, "Author:", get_authors())
        self.section_combo = self._create_combo(container, "Section:", get_sections())
        self.publisher_combo = self._create_combo(container, "Publisher:", get_publishers())
        self.language_entry = self._create_field(container, "Language:")
        self.status_combo = self._create_combo(
            container,
            "Status:",
            ["available", "reserved", "lost", "maintenance"]
        )

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
            text="Save Book",
            width=120,
            height=38,
            fg_color="#1a5f3d",
            hover_color="#236b49",
            command=self.save
        )
        btn_save.pack(side="right")

    # Small UI factory helper to keep the main layout code cleaner.
    def _create_field(self, parent, label_text):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 12))

        label = ctk.CTkLabel(frame, text=label_text, font=ctk.CTkFont(size=13))
        label.pack(anchor="w", pady=(0, 4))

        entry = ctk.CTkEntry(frame, height=36)
        entry.pack(fill="x")
        return entry

    # Small UI factory helper to keep the main layout code cleaner.
    def _create_combo(self, parent, label_text, values):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 12))

        label = ctk.CTkLabel(frame, text=label_text, font=ctk.CTkFont(size=13))
        label.pack(anchor="w", pady=(0, 4))

        combo = ctk.CTkComboBox(frame, height=36, values=values)
        if values:
            combo.set(values[0])
        combo.pack(fill="x")
        return combo

    # Validate form input and persist changes to the database.
    def save(self):
        title = self.title_entry.get().strip()
        if not title:
            messagebox.showwarning("Validation", "Title is required!")
            return

        data = {
            "title": title,
            "author": self.author_combo.get(),
            "section": self.section_combo.get(),
            "publisher": self.publisher_combo.get(),
            "language": self.language_entry.get().strip(),
            "status": self.status_combo.get()
        }

        if add_book(data):
            messagebox.showinfo("Success", "Book added successfully!")
            self.callback()
            self.destroy()
        else:
            messagebox.showerror("Error", "Failed to add book.")


# Main class: EditBookDialog (defined in books_view.py).
class EditBookDialog(ctk.CTkToplevel):
    # Build the UI for this window/frame and wire up callbacks.
    def __init__(self, parent, book_data, callback):
        super().__init__(parent)
        self.book_id = book_data[0]
        self.callback = callback
        self.current_status = book_data[6]  # Status is at index 6 now (it used to be index 5).

        # Read the current language value from book_data.
        self.current_language = book_data[5]  # Language is at index 5.

        self.title("Edit Book")
        self.geometry("500x680")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=24, pady=24)

        title = ctk.CTkLabel(
            container,
            text="Edit Book",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title.pack(pady=(0, 20))

        self.title_entry = self._create_field(container, "Title:")
        self.title_entry.insert(0, book_data[1])

        self.author_combo = self._create_combo(container, "Author:", get_authors())
        self.author_combo.set(book_data[2])

        self.section_combo = self._create_combo(container, "Section:", get_sections())
        self.section_combo.set(book_data[3])

        self.publisher_combo = self._create_combo(container, "Publisher:", get_publishers())
        self.publisher_combo.set(book_data[4])

        self.language_entry = self._create_field(container, "Language:")
        # Pre-fill the current language value.
        if self.current_language:
            self.language_entry.insert(0, self.current_language)

        # Status handling.
        if self.current_status == "borrowed":
            # If borrowed, display it as locked (cannot edit here).
            status_frame = ctk.CTkFrame(container, fg_color="transparent")
            status_frame.pack(fill="x", pady=(0, 12))

            status_label = ctk.CTkLabel(status_frame, text="Status:", font=ctk.CTkFont(size=13))
            status_label.pack(anchor="w", pady=(0, 4))

            status_value = ctk.CTkLabel(
                status_frame,
                text="borrowed (locked)",
                fg_color="#dc2626",
                text_color="white",
                corner_radius=8,
                height=36,
                anchor="w",
                padx=12,
                font=ctk.CTkFont(size=13, weight="bold")
            )
            status_value.pack(fill="x")

            info = ctk.CTkLabel(
                container,
                text="ℹ️ This book is currently borrowed. Status can only be changed via the Loans → Return process.",
                font=ctk.CTkFont(size=11),
                text_color="#dc2626",
                wraplength=440,
                justify="left"
            )
            info.pack(pady=(0, 10))

            self.status_combo = None  # No status combobox in this locked/borrowed case.
        else:
            # Normal case: status can be changed.
            self.status_combo = self._create_combo(
                container,
                "Status:",
                ["available", "reserved", "lost", "maintenance"]
            )
            self.status_combo.set(self.current_status)

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
            text="Update Book",
            width=120,
            height=38,
            fg_color="#1a5f3d",
            hover_color="#236b49",
            command=self.save
        )
        btn_save.pack(side="right")

    # Small UI factory helper to keep the main layout code cleaner.
    def _create_field(self, parent, label_text):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 12))

        label = ctk.CTkLabel(frame, text=label_text, font=ctk.CTkFont(size=13))
        label.pack(anchor="w", pady=(0, 4))

        entry = ctk.CTkEntry(frame, height=36)
        entry.pack(fill="x")
        return entry

    # Small UI factory helper to keep the main layout code cleaner.
    def _create_combo(self, parent, label_text, values):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=(0, 12))

        label = ctk.CTkLabel(frame, text=label_text, font=ctk.CTkFont(size=13))
        label.pack(anchor="w", pady=(0, 4))

        combo = ctk.CTkComboBox(frame, height=36, values=values)
        combo.pack(fill="x")
        return combo

    # Validate form input and persist changes to the database.
    def save(self):
        title = self.title_entry.get().strip()
        if not title:
            messagebox.showwarning("Validation", "Title is required!")
            return

        # If there is no status combo (borrowed case), keep the current status.
        new_status = self.status_combo.get() if self.status_combo else self.current_status

        # Language: if left blank, keep the existing value.
        new_language = self.language_entry.get().strip()
        if not new_language:
            new_language = self.current_language  # Use the existing value.

        data = {
            "book_id": self.book_id,
            "title": title,
            "author": self.author_combo.get(),
            "section": self.section_combo.get(),
            "publisher": self.publisher_combo.get(),
            "language": new_language,  # If blank, the previous value will be kept.
            "status": new_status,
            "current_status": self.current_status  # Send the current status as well.
        }

        result = update_book(data)

        if result["success"]:
            messagebox.showinfo("Success", "Book updated successfully!")
            self.callback()
            self.destroy()
        else:
            # Show a user-friendly error message.
            messagebox.showerror("Error", result["message"])
