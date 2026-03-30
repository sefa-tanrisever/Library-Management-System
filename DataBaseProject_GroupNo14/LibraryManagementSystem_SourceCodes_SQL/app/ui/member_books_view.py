# app/ui/member_books_view.py
# Member-facing book browsing screen: shows the inventory (read-only) with search + language filter.


import customtkinter as ctk  # Modern themed Tk widgets
from app.repositories.books_repo import list_books, get_books_stats  # Data access (books + stats)
from app.ui.modern_table_styles import ModernTable, StatCard  # Reusable table + stat card UI components
from app.repositories.books_repo import get_languages  # Helper to populate the language dropdown


class MemberBooksView(ctk.CTkFrame):
    def __init__(self, master, user_data):
        super().__init__(master, fg_color="#f0f0f0")
        self.user_data = user_data  # Current logged-in member info
        self.pack_propagate(False)

        # Main container for spacing and consistent layout
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Header: title + welcome message
        header = ctk.CTkFrame(container, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))

        title = ctk.CTkLabel(
            header,
            text="Browse Books",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#2b2b2b"
        )
        title.pack(side="left")

        # Friendly greeting (member-specific)
        welcome = ctk.CTkLabel(
            header,
            text=f"Welcome, {self.user_data['name']}! 👋",
            font=ctk.CTkFont(size=14),
            text_color="#1a5f3d"
        )
        welcome.pack(side="right")

        # Stats cards (member view shows fewer stats than staff view)
        self.stats_frame = ctk.CTkFrame(container, fg_color="transparent")
        self.stats_frame.pack(fill="x", pady=(0, 20))
        self.stats_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Toolbar: search + language filter
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
        self.search_entry.bind("<Return>", lambda e: self.load())  # Enter triggers search

        # Language filter dropdown (includes "All Languages" option)
        self.language_filter = ctk.CTkComboBox(
            toolbar_content,
            values=["All Languages"] + get_languages(),
            width=150,
            height=38,
            font=ctk.CTkFont(size=13),
            command=lambda _: self.load()  # Reload on selection change
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

        # Info banner (member guidance)
        info_banner = ctk.CTkFrame(container, corner_radius=12, fg_color="#e0f2fe")
        info_banner.pack(fill="x", pady=(0, 20))

        info_content = ctk.CTkFrame(info_banner, fg_color="transparent")
        info_content.pack(fill="x", padx=20, pady=12)

        info_icon = ctk.CTkLabel(
            info_content,
            text="ℹ️",
            font=ctk.CTkFont(size=18),
            text_color="#0369a1"
        )
        info_icon.pack(side="left", padx=(0, 12))

        info_text = ctk.CTkLabel(
            info_content,
            text="Browse our collection of books. Contact library staff to borrow books.",
            font=ctk.CTkFont(size=12),
            text_color="#0369a1"
        )
        info_text.pack(side="left")

        # Table area (book list)
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

        # Table columns are same as staff view, but member has no edit/delete actions
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
        self.table.pack(fill="both", expand=True)

        # Initial load
        self.load_stats()
        self.load()

    def load_stats(self):
        # Fetch global stats from repository and rebuild cards
        stats = get_books_stats()

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
        ).grid(row=0, column=2, sticky="ew")

    def refresh(self):
        # Reset filters and reload the table
        self.search_entry.delete(0, "end")
        self.language_filter.set("All Languages")
        self.load_stats()
        self.load()

    def load(self):
        # Apply search + language filter then refresh the table rows
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
            # Add status tags for styling (available/borrowed)
            status = r[6]
            status_tags = []
            if status == "available":
                status_tags.append("available")
            elif status == "borrowed":
                status_tags.append("borrowed")

            self.table.insert_row(r, tags=status_tags)
