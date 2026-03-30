# app/main.py

import customtkinter as ctk  # UI framework (the whole app uses CustomTkinter)
from app.ui.login_window import LoginWindow  # First screen: user authentication
from app.ui.app_window import AppWindow  # Main application window after login


def main():
    # Global UI theme settings (applies to all CustomTkinter widgets)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Login loop - logout yapınca tekrar login'e döner
    # Loop: after logout we show the login screen again.
    while True:
        # Show login window (blocking until closed)
        login_window = LoginWindow()
        login_window.mainloop()

        # If user closes the login window without successful auth -> exit app
        if not login_window.login_successful:
            break

        # Open the main app window using the authenticated user's info
        app = AppWindow(user_data=login_window.user_data)
        app.mainloop()

        # If the user did NOT request logout, they closed the app entirely -> exit
        if not hasattr(app, 'logout_requested') or not app.logout_requested:
            break

        # If logout_requested is True, the loop continues and login appears again


if __name__ == "__main__":
    # Standard Python entry point (allows running with: python main.py)
    main()
