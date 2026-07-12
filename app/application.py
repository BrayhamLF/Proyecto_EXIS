"""
application.py
--------------

Ventana principal de la aplicación.

Responsabilidades:
- Configurar la ventana principal.
- Administrar la navegación entre páginas.
- Servir como punto de entrada de la interfaz.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.settings import Settings

from views.auth.login_page import LoginPage


class Application(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.current_page = None

        self._configure_window()

        self._center_window()

        self.show_login()

    # =====================================================
    # CONFIGURACIÓN
    # =====================================================

    def _configure_window(self):

        self.title(Settings.APP_NAME)

        self.geometry(
            f"{Settings.WINDOW_WIDTH}x{Settings.WINDOW_HEIGHT}"
        )

        self.minsize(
            Settings.MIN_WIDTH,
            Settings.MIN_HEIGHT
        )

        self.configure(
            fg_color=Colors.BACKGROUND
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        self.grid_columnconfigure(
            0,
            weight=1
        )

    # =====================================================
    # CENTRAR VENTANA
    # =====================================================

    def _center_window(self):

        self.update_idletasks()

        width = Settings.WINDOW_WIDTH
        height = Settings.WINDOW_HEIGHT

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(
            f"{width}x{height}+{x}+{y}"
        )

    # =====================================================
    # LOGIN
    # =====================================================

    def show_login(self):

        self.clear_page()

        self.current_page = LoginPage(
            self,
            login_callback=self.login
        )

        self.current_page.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

    # =====================================================
    # AUTENTICACIÓN
    # =====================================================

    def login(
        self,
        email,
        password,
        role
    ):
        """
        Temporalmente solo imprime los datos.

        En el Sprint 3 se conectará con
        el AuthenticationController.
        """

        print("===== LOGIN =====")
        print("Correo:", email)
        print("Rol:", role)

        # TODO:
        # self.show_main_layout()

    # =====================================================
    # NAVEGACIÓN
    # =====================================================

    def clear_page(self):

        if self.current_page is not None:

            self.current_page.destroy()

            self.current_page = None

    def show_page(
        self,
        page_class,
        *args,
        **kwargs
    ):

        self.clear_page()

        self.current_page = page_class(
            self,
            *args,
            **kwargs
        )

        self.current_page.grid(
            row=0,
            column=0,
            sticky="nsew"
        )