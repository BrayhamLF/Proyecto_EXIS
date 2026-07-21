"""
settings_header.py
------------------

Encabezado del módulo Configuración.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class SettingsHeader(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0, weight=1)

        self._build()

    # ==================================================
    # Construcción
    # ==================================================

    def _build(self):

        # Categoría

        category = ctk.CTkLabel(

            self,

            text="CUENTA",

            font=Fonts.SMALL_BOLD,

            text_color=Colors.SECONDARY,

            anchor="w"

        )

        category.grid(

            row=0,

            column=0,

            sticky="w"

        )

        # -----------------------------------------

        title = ctk.CTkLabel(

            self,

            text="Configuración",

            font=Fonts.H1,

            text_color=Colors.PRIMARY,

            anchor="w"

        )

        title.grid(

            row=1,

            column=0,

            sticky="w",

            pady=(4, 6)

        )

        # -----------------------------------------

        subtitle = ctk.CTkLabel(

            self,

            text="Ajustes de la cuenta institucional.",

            font=Fonts.BODY,

            text_color=Colors.TEXT_SECONDARY,

            anchor="w"

        )

        subtitle.grid(

            row=2,

            column=0,

            sticky="w"

        )

        # -----------------------------------------

        separator = ctk.CTkFrame(

            self,

            height=1,

            fg_color=Colors.BORDER

        )

        separator.grid(

            row=3,

            column=0,

            sticky="ew",

            pady=(18, 0)

        )