# app/ui/modern_table_styles.py

"""
Modern table styling utilities for the Library Management System.
Provides consistent, clean data-table layouts across all views.
"""

from tkinter import ttk  # ttk provides the Treeview widget (table) + styling via ttk.Style()
import customtkinter as ctk  # CustomTkinter components for a modern-looking UI


def apply_modern_table_style():
    """
    Apply modern, clean styling to ttk.Treeview widgets.
    Features:
    - Distinct header with strong background
    - Increased row height and padding
    - Zebra striping
    - Subtle borders
    - Professional typography
    """
    style = ttk.Style()  # Central style controller for all ttk widgets in this app

    # Use "clam" theme as a reliable base (works consistently across platforms)
    try:
        style.theme_use("clam")
    except:
        # If the theme is not available, we silently continue with the default theme
        pass

    # Main Treeview styling (rows/cells)
    style.configure(
        "Modern.Treeview",
        background="#ffffff",         # table background
        foreground="#1f2937",         # default text color
        fieldbackground="#ffffff",    # background behind cells
        borderwidth=0,
        relief="flat",
        rowheight=40,  # Increased for better readability
        font=("Segoe UI", 11),
    )

    # Header styling (column titles)
    style.configure(
        "Modern.Treeview.Heading",
        background="#1a5f3d",
        foreground="#ffffff",
        relief="flat",
        borderwidth=0,
        font=("Segoe UI", 11, "bold"),
        padding=(16, 12),
    )

    # Hover/selection effects for better UX feedback
    style.map(
        "Modern.Treeview",
        background=[
            ("selected", "#40a170"),  # selected row background
            ("active", "#f3f4f6")     # hover background
        ],
        foreground=[
            ("selected", "#ffffff"),  # selected row text color
            ("active", "#1f2937")     # hover text color
        ]
    )

    # Header hover effect (subtle color change)
    style.map(
        "Modern.Treeview.Heading",
        background=[("active", "#236b49")],
        foreground=[("active", "#ffffff")]
    )

    # Configure alternating row colors (zebra striping)
    # (We still apply row tags per-row; this keeps the row height consistent here too.)
    style.configure("Modern.Treeview", rowheight=40)


class ModernTable(ctk.CTkFrame):
    """
    A modern table component that wraps ttk.Treeview with:
    - Custom styling
    - Modern scrollbar
    - Zebra striping
    - Clean borders
    """

    def __init__(self, master, columns, column_configs=None, **kwargs):
        """
        Args:
            master: Parent widget
            columns: Tuple of column identifiers
            column_configs: Dict mapping column_id to config dict with:
                - heading: Column heading text
                - width: Column width in pixels
                - anchor: Text alignment ("w", "center", "e")
        """
        super().__init__(master, fg_color="transparent", **kwargs)

        # Ensure Treeview has our theme/styles applied before creating the widget
        apply_modern_table_style()

        # Outer container gives a "card" feel (rounded corners + border)
        self.table_container = ctk.CTkFrame(
            self,
            fg_color="#ffffff",
            corner_radius=12,
            border_width=1,
            border_color="#e5e7eb"
        )
        self.table_container.pack(fill="both", expand=True)

        # Inner container adds a tiny padding so the Treeview doesn't touch the border
        inner_container = ctk.CTkFrame(
            self.table_container,
            fg_color="transparent"
        )
        inner_container.pack(fill="both", expand=True, padx=2, pady=2)

        # Make Treeview expand to fill available space
        inner_container.grid_rowconfigure(0, weight=1)
        inner_container.grid_columnconfigure(0, weight=1)

        # Create the actual table widget (Treeview used like a multi-column table)
        self.tree = ttk.Treeview(
            inner_container,
            columns=columns,
            show="headings",         # hide the first "tree" column and show only headings
            selectmode="browse",     # single-row selection
            style="Modern.Treeview"
        )
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Configure each column: heading text, width, and alignment
        if column_configs:
            for col_id, config in column_configs.items():
                self.tree.heading(
                    col_id,
                    text=config.get("heading", col_id),
                    anchor=config.get("heading_anchor", "w")
                )
                self.tree.column(
                    col_id,
                    width=config.get("width", 100),
                    anchor=config.get("anchor", "w"),
                    minwidth=config.get("minwidth", 50)
                )

        # CustomTkinter scrollbar (looks better than default ttk scrollbar)
        scrollbar = ctk.CTkScrollbar(
            inner_container,
            orientation="vertical",
            command=self.tree.yview,
            width=16,
            corner_radius=8,
            fg_color="#f3f4f6",
            button_color="#9ca3af",
            button_hover_color="#6b7280"
        )
        scrollbar.grid(row=0, column=1, sticky="ns", padx=(4, 0))
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Zebra striping tags (we assign these on insert_row)
        self.tree.tag_configure("oddrow", background="#f0f8ff")
        self.tree.tag_configure("evenrow", background="#fffafa")

        # Status color tags used across the app (books, loans, overdue, etc.)
        self.tree.tag_configure("available", foreground="#2f2f2f", font=("Segoe UI", 11))
        self.tree.tag_configure("borrowed", foreground="#dc2626", font=("Segoe UI", 11))
        self.tree.tag_configure("overdue", foreground="#dc2626", font=("Segoe UI", 11, "bold"))
        self.tree.tag_configure("returned", foreground="#16a34a", font=("Segoe UI", 11))
        self.tree.tag_configure("critical", foreground="#991b1b", font=("Segoe UI", 11, "bold"))
        self.tree.tag_configure("moderate", foreground="#ea580c", font=("Segoe UI", 11))
        self.tree.tag_configure("recent", foreground="#f59e0b", font=("Segoe UI", 11))

    def insert_row(self, values, tags=None, **kwargs):
        """Insert a row with automatic zebra striping"""
        # Decide zebra tag based on current row count
        row_count = len(self.tree.get_children())
        zebra_tag = "evenrow" if row_count % 2 == 0 else "oddrow"

        # Merge zebra tag with any additional tags (status/severity tags)
        if tags:
            if isinstance(tags, str):
                tags = (zebra_tag, tags)
            else:
                tags = (zebra_tag,) + tuple(tags)
        else:
            tags = (zebra_tag,)

        return self.tree.insert("", "end", values=values, tags=tags, **kwargs)

    def clear(self):
        """Clear all rows from the table"""
        for item in self.tree.get_children():
            self.tree.delete(item)

    def get_selected_values(self):
        """Get values of the selected row"""
        selection = self.tree.selection()
        if selection:
            return self.tree.item(selection[0])["values"]
        return None


class StatCard(ctk.CTkFrame):
    """Modern stat card component"""

    def __init__(self, master, title, value, icon, color, **kwargs):
        # This is basically a reusable colored "info tile" used in multiple screens
        super().__init__(
            master,
            corner_radius=12,
            fg_color=color,
            **kwargs
        )

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=16)

        # Icon (emoji) to visually represent the stat
        icon_label = ctk.CTkLabel(
            content,
            text=icon,
            font=ctk.CTkFont(size=32),
            text_color="white"
        )
        icon_label.pack(anchor="w")

        # Small title label (e.g., "Total Books")
        title_label = ctk.CTkLabel(
            content,
            text=title,
            font=ctk.CTkFont(size=12),
            text_color="white"
        )
        title_label.pack(anchor="w", pady=(8, 2))

        # Main value (big number)
        self.value_label = ctk.CTkLabel(
            content,
            text=str(value),
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white"
        )
        self.value_label.pack(anchor="w")

    def update_value(self, new_value):
        """Update the stat card value"""
        self.value_label.configure(text=str(new_value))
