# app/ui/app_window.py
# Main application window: shows the sidebar navigation and routes the user to different pages based on their role.

# CustomTkinter provides modern-looking themed Tk widgets (frames, labels, buttons, etc.).
import customtkinter as ctk
# Tkinter messagebox is used for simple pop-up dialogs (info / warning / confirm).
from tkinter import messagebox
# Other UI pages/components that are loaded into the main window.
from app.ui.books_view import BooksView
from app.ui.members_view import MembersView
from app.ui.loans_view import LoansView
from app.ui.overdue_view import OverdueView
from app.ui.member_books_view import MemberBooksView
from app.ui.member_loans_view import MemberLoansView


# Main class: AppWindow (defined in app_window.py).
class AppWindow(ctk.CTk):
    # Build the UI for this window/frame and wire up callbacks.
    def __init__(self, user_data=None):
        super().__init__()

        # Keep basic identity/role info for navigation + page permissions.
        self.user_data = user_data or {"name": "User", "email": "", "role": "member", "id": None}

        # Flag used by main loop to decide whether we should return to login.
        self.logout_requested = False

        # Window title + default size constraints.
        self.title("Library Management System")
        self.geometry("1400x800")
        self.minsize(1200, 700)

        # Main layout: 2 columns (sidebar + content), 1 row.
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Sidebar: fixed width, custom green theme.
        self.sidebar = ctk.CTkFrame(self, width=240, corner_radius=0, fg_color="#1a5f3d")
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(10, weight=1)  # push logout to the bottom
        self.sidebar.grid_propagate(False)  # keep sidebar width stable

        # Logo / brand area (top of sidebar).
        logo_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        logo_frame.grid(row=0, column=0, padx=20, pady=(30, 20), sticky="ew")

        brand = ctk.CTkLabel(
            logo_frame,
            text="📚 Library",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="white"
        )
        brand.pack(anchor="w")

        sub = ctk.CTkLabel(
            logo_frame,
            text="Management System",
            font=ctk.CTkFont(size=12),
            text_color="#c9e4d9"
        )
        sub.pack(anchor="w", pady=(2, 0))

        # Small user card (shows name + role).
        user_frame = ctk.CTkFrame(self.sidebar, fg_color="#144d31", corner_radius=8)
        user_frame.grid(row=1, column=0, padx=16, pady=(10, 20), sticky="ew")

        user_label = ctk.CTkLabel(
            user_frame,
            text=f"👤 {self.user_data['name']}",
            font=ctk.CTkFont(size=11),
            text_color="white"
        )
        user_label.pack(padx=12, pady=(8, 4))

        role_label = ctk.CTkLabel(
            user_frame,
            text=f"Role: {self.user_data['role'].title()}",
            font=ctk.CTkFont(size=9),
            text_color="#c9e4d9"
        )
        role_label.pack(padx=12, pady=(0, 8))

        # Navigation buttons are created dynamically depending on the user role.
        self.nav_buttons = {}
        self._create_navigation_menu()

        # Bottom logout button (always visible).
        exit_btn = ctk.CTkButton(
            self.sidebar,
            text="Logout",
            font=ctk.CTkFont(size=13),
            fg_color="#144d31",
            hover_color="#0f3d26",
            height=40,
            command=self.logout
        )
        exit_btn.grid(row=11, column=0, padx=16, pady=20, sticky="ew")

        # Content area (right side): pages get packed into this frame.
        self.content = ctk.CTkFrame(self, corner_radius=0, fg_color="#f0f0f0")
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        # Track which page is currently shown to avoid unnecessary re-renders.
        self.current_page = None

        # Default landing page depends on role:
        # - member: can only browse books + see own loans
        # - staff/admin: start on full Books management view
        if self.user_data['role'] == 'member':
            self.show_page("member_books")
        else:
            self.show_page("books")

    # Small UI factory helper to keep the main layout code cleaner.
    def _create_navigation_menu(self):
        """Create navigation menu based on user role"""
        role = self.user_data['role']
        row = 2

        if role == 'member':
            # Member can only see books and their own loans.
            self.nav_buttons["member_books"] = self._create_nav_button(
                "📚  Browse Books", row, lambda: self.show_page("member_books")
            )
            row += 1

            self.nav_buttons["member_loans"] = self._create_nav_button(
                "📋  My Loans", row, lambda: self.show_page("member_loans")
            )
            row += 1

        else:
            # Librarian and Admin have full access (inventory + members + loans + overdue).
            self.nav_buttons["books"] = self._create_nav_button(
                "📚  Books", row, lambda: self.show_page("books")
            )
            row += 1

            self.nav_buttons["members"] = self._create_nav_button(
                "👥  Members", row, lambda: self.show_page("members")
            )
            row += 1

            self.nav_buttons["loans"] = self._create_nav_button(
                "📋  Loans", row, lambda: self.show_page("loans")
            )
            row += 1

            self.nav_buttons["overdue"] = self._create_nav_button(
                "⏰  Overdue", row, lambda: self.show_page("overdue")
            )
            row += 1

    # Small UI factory helper to keep the main layout code cleaner.
    def _create_nav_button(self, text: str, row: int, command):
        # Sidebar buttons are styled as "flat" entries (transparent background),
        # then we color the active one in _highlight_active_button().
        btn = ctk.CTkButton(
            self.sidebar,
            text=text,
            anchor="w",
            font=ctk.CTkFont(size=14),
            fg_color="transparent",
            text_color="white",
            hover_color="#236b49",
            height=45,
            command=command
        )
        btn.grid(row=row, column=0, padx=16, pady=4, sticky="ew")
        return btn

    # Visually mark the active page in the sidebar.
    def _highlight_active_button(self, page: str):
        """Highlight the active navigation button"""
        for key, btn in self.nav_buttons.items():
            if key == page:
                btn.configure(fg_color="#236b49", text_color="white")
            else:
                btn.configure(fg_color="transparent", text_color="white")

    def clear_content(self):
        # Remove the old page widgets before loading the new page.
        for w in self.content.winfo_children():
            w.destroy()

    def show_page(self, page: str):
        # Avoid reloading if the requested page is already active.
        if self.current_page == page:
            return

        self.current_page = page
        self.clear_content()
        self._highlight_active_button(page)

        # Member pages (limited access).
        if page == "member_books":
            MemberBooksView(self.content, self.user_data).pack(fill="both", expand=True)
        elif page == "member_loans":
            MemberLoansView(self.content, self.user_data).pack(fill="both", expand=True)

        # Staff/Admin pages (full access).
        elif page == "books":
            BooksView(self.content).pack(fill="both", expand=True)
        elif page == "members":
            MembersView(self.content).pack(fill="both", expand=True)
        elif page == "loans":
            LoansView(self.content).pack(fill="both", expand=True)
        elif page == "overdue":
            OverdueView(self.content).pack(fill="both", expand=True)

    # Ask for confirmation, then close the app and return to the login screen.
    def logout(self):
        """Handle logout - return to login screen"""
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.logout_requested = True
            self.destroy()
