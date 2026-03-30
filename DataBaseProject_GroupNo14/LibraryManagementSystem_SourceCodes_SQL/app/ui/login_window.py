# app/ui/login_window.py
# Login window: authenticates either staff (librarian/admin) or a member, then closes itself on success.


import customtkinter as ctk  # Modern themed Tk widgets
from tkinter import messagebox  # Pop-up dialogs for validation/errors
from app.repositories.auth_repo import authenticate_user, authenticate_member  # Repo auth functions


class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Basic window configuration
        self.title("Library Management System - Login")
        self.geometry("1100x700")
        self.resizable(False, False)

        # Configure a 2-column grid: left decorative panel + right login form
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Left side - Decorative panel (branding / visuals)
        self.left_panel = ctk.CTkFrame(
            self,
            fg_color=("#1a1a2e", "#16213e"),
            corner_radius=0
        )
        self.left_panel.grid(row=0, column=0, sticky="nsew")

        # Add decorative elements to left panel
        self._create_decorative_elements()

        # Right side - Login form container
        self.right_panel = ctk.CTkFrame(
            self,
            fg_color=("#ffffff", "#ffffff"),
            corner_radius=0
        )
        self.right_panel.grid(row=0, column=1, sticky="nsew")

        # Create login form
        self._create_login_form()

        # Store login result (read by the caller after window closes)
        self.login_successful = False
        self.user_data = None

    def _create_decorative_elements(self):
        """Create decorative elements on the left panel"""
        container = ctk.CTkFrame(self.left_panel, fg_color="transparent")
        container.place(relx=0.5, rely=0.5, anchor="center")

        # Large icon/logo
        logo_label = ctk.CTkLabel(
            container,
            text="📚",
            font=ctk.CTkFont(size=120),
        )
        logo_label.pack(pady=(0, 20))

        # App name
        app_name = ctk.CTkLabel(
            container,
            text="Library",
            font=ctk.CTkFont(size=42, weight="bold"),
            text_color=("#ffffff", "#ffffff")
        )
        app_name.pack(pady=(0, 5))

        # Subtitle
        subtitle = ctk.CTkLabel(
            container,
            text="Management System",
            font=ctk.CTkFont(size=18),
            text_color=("#b8b8b8", "#c9e4d9")
        )
        subtitle.pack()

        # Decorative circles (purely visual)
        circle1 = ctk.CTkLabel(
            self.left_panel,
            text="●",
            font=ctk.CTkFont(size=200),
            text_color=("#8b2f97", "#9c4aa8")
        )
        circle1.place(relx=0.2, rely=0.7, anchor="center")

        circle2 = ctk.CTkLabel(
            self.left_panel,
            text="●",
            font=ctk.CTkFont(size=150),
            text_color=("#d946a8", "#ec4899")
        )
        circle2.place(relx=0.8, rely=0.3, anchor="center")

    def _create_login_form(self):
        """Create the login form on the right panel"""
        # Form container (centered)
        form_container = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        form_container.place(relx=0.5, rely=0.5, anchor="center")

        # Welcome text
        welcome_label = ctk.CTkLabel(
            form_container,
            text="Welcome Back!",
            font=ctk.CTkFont(size=36, weight="bold"),
            text_color=("#6b21a8", "#7c3aed")
        )
        welcome_label.pack(pady=(0, 10))

        # Subtitle
        subtitle_label = ctk.CTkLabel(
            form_container,
            text="Sign in to your account",
            font=ctk.CTkFont(size=14),
            text_color=("#9ca3af", "#6b7280")
        )
        subtitle_label.pack(pady=(0, 40))

        # Email field container
        email_container = ctk.CTkFrame(form_container, fg_color="transparent")
        email_container.pack(fill="x", pady=(0, 20))

        email_label_frame = ctk.CTkFrame(email_container, fg_color="transparent")
        email_label_frame.pack(fill="x", pady=(0, 8))

        email_icon = ctk.CTkLabel(
            email_label_frame,
            text="✉",
            font=ctk.CTkFont(size=16),
            text_color=("#6b21a8", "#7c3aed")
        )
        email_icon.pack(side="left", padx=(0, 8))

        email_label = ctk.CTkLabel(
            email_label_frame,
            text="Email:",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=("#6b21a8", "#7c3aed"),
            anchor="w"
        )
        email_label.pack(side="left")

        # Email input (Enter jumps to password)
        self.email_entry = ctk.CTkEntry(
            email_container,
            width=400,
            height=50,
            font=ctk.CTkFont(size=13),
            corner_radius=8,
            border_width=2,
            border_color=("#6b21a8", "#7c3aed"),
            fg_color=("#ffffff", "#ffffff"),
            text_color=("#1f2937", "#1f2937")
        )
        self.email_entry.pack()
        self.email_entry.bind("<Return>", lambda e: self.password_entry.focus())

        # Password field container
        password_container = ctk.CTkFrame(form_container, fg_color="transparent")
        password_container.pack(fill="x", pady=(0, 35))

        password_label_frame = ctk.CTkFrame(password_container, fg_color="transparent")
        password_label_frame.pack(fill="x", pady=(0, 8))

        password_icon = ctk.CTkLabel(
            password_label_frame,
            text="🔒",
            font=ctk.CTkFont(size=16),
            text_color=("#6b21a8", "#7c3aed")
        )
        password_icon.pack(side="left", padx=(0, 8))

        password_label = ctk.CTkLabel(
            password_label_frame,
            text="Password:",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=("#6b21a8", "#7c3aed"),
            anchor="w"
        )
        password_label.pack(side="left")

        # Password input (Enter attempts login)
        self.password_entry = ctk.CTkEntry(
            password_container,
            width=400,
            height=50,
            font=ctk.CTkFont(size=13),
            corner_radius=8,
            border_width=2,
            border_color=("#6b21a8", "#7c3aed"),
            fg_color=("#ffffff", "#ffffff"),
            text_color=("#1f2937", "#1f2937"),
            show="●"
        )
        self.password_entry.pack()
        self.password_entry.bind("<Return>", lambda e: self.login())

        # Login button (primary action)
        self.login_button = ctk.CTkButton(
            form_container,
            text="Login",
            width=400,
            height=50,
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color=("#6b21a8", "#7c3aed"),
            hover_color=("#581c87", "#6d28d9"),
            corner_radius=8,
            command=self.login
        )
        self.login_button.pack(pady=(0, 20))

        # Demo credentials note (for testing / grading)
        demo_info = ctk.CTkLabel(
            form_container,
            text="💡 Demo Accounts:\nStaff: staff1@library.com / 1234\nMember: ali@example.com / 1234",
            font=ctk.CTkFont(size=11),
            text_color=("#9ca3af", "#6b7280"),
            justify="center"
        )
        demo_info.pack(pady=(25, 0))

    def login(self):
        """Handle login button click"""
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        # Basic validation: both fields are required
        if not email or not password:
            messagebox.showwarning("Validation Error", "Please enter both email and password!")
            return

        # Try staff/librarian/admin authentication first
        user = authenticate_user(email, password)

        if user:
            self.login_successful = True
            self.user_data = user
            self.destroy()
            return

        # Then try member authentication
        member = authenticate_member(email, password)

        if member:
            self.login_successful = True
            self.user_data = member
            self.destroy()
            return

        # Authentication failed: show hint + demo credentials
        messagebox.showerror(
            "Login Failed",
            "Invalid email or password!\n\nDemo Accounts:\nStaff: staff1@library.com / 1234\nMember: ali@example.com / 1234"
        )
        self.password_entry.delete(0, "end")  # Clear password only (email stays)
