"""Ventana principal y punto de composición de la aplicación."""

from __future__ import annotations

import customtkinter as ctk

from app.router import Router
from app.routes import MAIN_ROUTES
from app.session import Session
from config.colors import Colors
from config.settings import Settings
from services.auth_service import AuthService
from views.auth.login_page import LoginPage
from views.layout.main_layout import MainLayout


class Application(ctk.CTk):
    """Ensambla dependencias y coordina el flujo público/autenticado."""

    def __init__(self, auth_service: AuthService | None = None):
        super().__init__()

        self.title(Settings.APP_NAME)
        self.geometry(f"{Settings.WINDOW_WIDTH}x{Settings.WINDOW_HEIGHT}")
        self.minsize(Settings.MIN_WIDTH, Settings.MIN_HEIGHT)
        self.configure(fg_color=Colors.BACKGROUND)

        self.router = Router(self)
        self.session = Session()
        self.auth_service = auth_service or AuthService()

        self.show_login()

    @property
    def current_view(self):
        """Vista raíz actual; se conserva para compatibilidad."""
        return self.router.current

    def clear_view(self) -> None:
        self.router.clear()

    def show_login(self) -> None:
        self.router.navigate(LoginPage(self, login_callback=self.login))

    def login(self, email: str, password: str, role: str) -> None:
        self.session = self.auth_service.authenticate(email, password, role)
        self.show_main_layout()

    def show_main_layout(self) -> None:
        layout = MainLayout(self, logout_callback=self.logout)
        self.router.navigate(layout)
        layout.set_user(self.session.full_name, self.session.role)
        layout.register_pages(MAIN_ROUTES)
        layout.show_default_page()

    def logout(self) -> None:
        """Cierra la sesión y vuelve al único punto de entrada público."""
        self.session.clear()
        self.show_login()
