"""
main_layout.py
--------------

Layout principal de la aplicación.

Responsabilidades:
- Organizar la interfaz principal.
- Administrar la navegación entre páginas.
- Coordinar Sidebar, Header y StatusBar.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors

from components.layout.sidebar import Sidebar
from components.layout.status_bar import StatusBar


class MainLayout(ctk.CTkFrame):

    SIDEBAR_WIDTH = 260
    HEADER_HEIGHT = 72
    STATUS_HEIGHT = 34

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=Colors.BACKGROUND
        )

        # -----------------------------
        # Administrador de páginas
        # -----------------------------

        self.pages: dict[type, ctk.CTkFrame] = {}
        self.current_page: ctk.CTkFrame | None = None

        # Diccionario de navegación
        # Se llenará cuando existan las páginas.
        self.routes = {}

        # -----------------------------
        # Grid principal
        # -----------------------------

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self._build()

    # ==========================================================
    # CONSTRUCCIÓN
    # ==========================================================

    def _build(self):

        # Sidebar

        self.sidebar = Sidebar(
            self,
            width=self.SIDEBAR_WIDTH,
            command=self._on_navigation
        )

        self.sidebar.grid(
            row=0,
            column=0,
            rowspan=3,
            sticky="nsew"
        )

        # Contenedor de páginas

        self.content = ctk.CTkFrame(
            self,
            fg_color=Colors.BACKGROUND
        )

        self.content.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=25,
            pady=20
        )

        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        # StatusBar

        self.status_bar = StatusBar(
            self,
            height=self.STATUS_HEIGHT
        )

        self.status_bar.grid(
            row=2,
            column=1,
            sticky="ew"
        )

    # ==========================================================
    # REGISTRO DE RUTAS
    # ==========================================================

    def register_pages(self, routes: dict):

        """
        Registra la relación:

            id_menu -> ClasePágina

        Ejemplo:

        {
            "dashboard": DashboardPage,
            "students": StudentPage
        }
        """

        self.routes = routes

    # ==========================================================
    # NAVEGACIÓN
    # ==========================================================

    def _on_navigation(self, option: str):

        if option == "logout":

            self.status_bar.set_message(
                "Cerrar sesión (pendiente de implementar)."
            )

            return

        page_class = self.routes.get(option)

        if page_class is None:

            self.status_bar.set_message(
                f"Módulo '{option}' aún no disponible."
            )

            return

        self.show_page(page_class)

    # ==========================================================
    # PAGE MANAGER
    # ==========================================================

    def show_page(
        self,
        page_class,
        *args,
        **kwargs
    ):

        # Crear la página una sola vez

        if page_class not in self.pages:

            page = page_class(
                self.content,
                *args,
                **kwargs
            )

            self.pages[page_class] = page

        else:

            page = self.pages[page_class]

        # Ocultar la actual

        if self.current_page is not None:

            if hasattr(self.current_page, "on_hide"):

                self.current_page.on_hide()

            self.current_page.grid_remove()

        # Mostrar la nueva

        page.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.current_page = page

        # Si la página implementa estos métodos, los invocamos

        if hasattr(page, "get_title"):

            self.header.set_title(
                page.get_title(),
                page.get_subtitle()
            )

        if hasattr(page, "on_show"):

            page.on_show()

        self.status_bar.set_message("Sistema listo.")

    # ==========================================================
    # API
    # ==========================================================

    def set_user(
        self,
        name: str,
        role: str
    ):

        self.header.set_user(
            name,
            role
        )

        self.sidebar.set_user(
            name,
            role
        )