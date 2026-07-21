"""
settings_layout.py
------------------

Layout principal del módulo Configuración.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors

from views.settings.components.settings_header import SettingsHeader
from views.settings.sections.password_section import PasswordSection


class SettingsLayout(ctk.CTkFrame):

    SECTION_SPACING = 24

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=Colors.BACKGROUND
        )

        self.header = None

        self.scroll = None
        self.content = None

        self.password_section = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build()

    # ==================================================
    # Construcción
    # ==================================================

    def _build(self):

        self._build_header()

        self._build_content()

    # ==================================================
    # Encabezado
    # ==================================================

    def _build_header(self):

        self.header = SettingsHeader(self)

        self.header.grid(

            row=0,

            column=0,

            sticky="ew",

            pady=(0, self.SECTION_SPACING)

        )

    # ==================================================
    # Contenido
    # ==================================================

    def _build_content(self):

        # ----------------------------------------------
        # Scroll principal
        # ----------------------------------------------

        self.scroll = ctk.CTkFrame(

            self,

            fg_color="transparent"

        )

        self.scroll.grid(

            row=1,

            column=0,

            sticky="nsew"

        )

        self.scroll.grid_columnconfigure(
            0,
            weight=1
        )

        # ----------------------------------------------
        # Contenedor interno
        # ----------------------------------------------

        self.content = ctk.CTkFrame(

            self.scroll,

            fg_color="transparent"

        )

        self.content.grid(

            row=0,

            column=0,

            sticky="ew",

            padx=5,

            pady=(0, 15)

        )

        self.content.grid_columnconfigure(
            0,
            weight=1
        )

        # ----------------------------------------------
        # Secciones
        # ----------------------------------------------

        self.password_section = PasswordSection(

            self.content

        )

        self.password_section.grid(

            row=0,

            column=0,

            sticky="ew"

        )