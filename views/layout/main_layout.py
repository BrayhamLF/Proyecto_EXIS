"""
main_layout.py
--------------

Layout principal de la aplicación.

Responsabilidades:
- Mostrar Header.
- Mostrar Sidebar.
- Mostrar StatusBar.
- Administrar la navegación.
- Administrar las páginas.
"""

from __future__ import annotations

from collections.abc import Callable

import customtkinter as ctk

from config.colors import Colors
from config.sizes import Sizes

from components.layout.sidebar import Sidebar
from components.layout.header import Header
from components.layout.status_bar import StatusBar


class MainLayout(ctk.CTkFrame):

    def __init__(
        self,
        master,
        logout_callback: Callable[[], None] | None = None,
    ):

        super().__init__(
            master,
            fg_color=Colors.BACKGROUND
        )

        # ==================================================
        # Administrador de páginas
        # ==================================================

        self.logout_callback = logout_callback
        self.pages: dict[type, ctk.CTkFrame] = {}
        self.current_page: ctk.CTkFrame | None = None
        self.routes: dict[str, type] = {}

        # ==================================================
        # Componentes
        # ==================================================

        self.sidebar: Sidebar | None = None
        self.header: Header | None = None
        self.content: ctk.CTkFrame | None = None
        self.status_bar: StatusBar | None = None

        # ==================================================
        # Layout
        # ==================================================

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self._build()

    # ==================================================
    # Construcción
    # ==================================================

    def _build(self):

        # ----------------------------------------------
        # Sidebar
        # ----------------------------------------------

        self.sidebar = Sidebar(
            self,
            width=Sizes.SIDEBAR_WIDTH,
            command=self._on_navigation
        )

        self.sidebar.grid(
            row=0,
            column=0,
            rowspan=3,
            sticky="nsew"
        )

        # ----------------------------------------------
        # Header
        # ----------------------------------------------

        self.header = Header(
            self,
            notification_callback=self.show_notifications,
        )

        self.header.grid(
            row=0,
            column=1,
            sticky="ew"
        )

        # ----------------------------------------------
        # Contenedor principal
        # ----------------------------------------------

        self.content = ctk.CTkFrame(
            self,
            fg_color=Colors.BACKGROUND,
            corner_radius=0
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

        # ----------------------------------------------
        # Barra de estado
        # ----------------------------------------------

        self.status_bar = StatusBar(
            self,
            height=Sizes.STATUSBAR_HEIGHT
        )

        self.status_bar.grid(
            row=2,
            column=1,
            sticky="ew"
        )

    # ==================================================
    # Registro de páginas
    # ==================================================

    def register_pages(
        self,
        routes: dict[str, type]
    ):

        if not isinstance(routes, dict):
            raise TypeError(
                "routes debe ser un diccionario."
            )

        self.routes = routes

    # ==================================================
    # Página inicial
    # ==================================================

    def show_default_page(self):

        if not self.routes:
            return

        first_page = next(iter(self.routes.values()))

        self.show_page(first_page)

    # ==================================================
    # Navegación
    # ==================================================

    def _on_navigation(self, option: str):

        if option == "logout":
            self.logout()
            return

        page_class = self.routes.get(option)

        if page_class is None:

            self.status_bar.set_message(
                f"Módulo '{option}' aún no disponible."
            )

            return

        self.show_page(page_class)

    # ==================================================
    # Mostrar página
    # ==================================================

    def show_page(
        self,
        page_class,
        *args,
        **kwargs
    ):

        # Ya está visible

        if (
            self.current_page is not None
            and isinstance(self.current_page, page_class)
        ):
            return

        # Crear una sola vez

        if page_class not in self.pages:

            page = page_class(
                self.content,
                *args,
                **kwargs
            )

            self.pages[page_class] = page

        else:

            page = self.pages[page_class]

        # Ocultar página anterior

        if self.current_page is not None:

            if hasattr(self.current_page, "on_hide"):
                self.current_page.on_hide()

            self.current_page.grid_remove()

        # Mostrar nueva

        page.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.current_page = page

        # Actualizar Header

        title = page.get_title() if hasattr(page, "get_title") else ""

        subtitle = (
            page.get_subtitle()
            if hasattr(page, "get_subtitle")
            else ""
        )

        self.header.set_title(
            title,
            subtitle
        )

        # Evento

        if hasattr(page, "on_show"):
            page.on_show()

        # StatusBar

        self.status_bar.set_message(
            f"{title} cargado correctamente."
        )

    # ==================================================
    # API
    # ==================================================

    def set_user(
        self,
        name: str,
        role: str
    ):

        self.header.set_user(
            name,
            role
        )

        if hasattr(self.sidebar, "set_user"):
            self.sidebar.set_user(
                name,
                role
            )

    # ==================================================
    # Sidebar
    # ==================================================

    def show_notifications(self):
        """Punto de extensión para el futuro panel de notificaciones."""
        self.status_bar.set_message("No tienes notificaciones pendientes.")

    # ==================================================
    # Utilidades
    # ==================================================

    def has_page(
        self,
        page_class
    ) -> bool:

        return page_class in self.pages

    def get_page(
        self,
        page_class
    ):

        return self.pages.get(page_class)

    def clear_pages(self):

        for page in self.pages.values():
            page.destroy()

        self.pages.clear()
        self.current_page = None

    # ==================================================
    # Logout
    # ==================================================

    def logout(self):

        self.status_bar.set_message(
            "Cerrando sesión..."
        )

        self.clear_pages()

        if self.logout_callback is not None:
            self.after_idle(self.logout_callback)

        # Application se encargará de mostrar
        # nuevamente la pantalla de Login.
