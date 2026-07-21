"""
empty_state.py
--------------

Estado vacío reutilizable para el Dashboard.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts

from utils.icons import Icons


class EmptyState(ctk.CTkFrame):

    def __init__(
        self,
        master,
        icon=None,
        title="Sin información",
        description=""
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.icon = icon

        self.title_text = title

        self.description_text = description

        self._build()

    # ======================================================

    def _build(self):

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ----------------------------------------------
        # Icono
        # ----------------------------------------------

        icon = ctk.CTkLabel(

            self,

            image=self.icon,

            text=""

        )

        icon.grid(
            row=1,
            column=0,
            pady=(0,18)
        )

        # ----------------------------------------------

        title = ctk.CTkLabel(

            self,

            text=self.title_text,

            font=Fonts.H3,

            text_color=Colors.TEXT

        )

        title.grid(
            row=2,
            column=0
        )

        # ----------------------------------------------

        description = ctk.CTkLabel(

            self,

            text=self.description_text,

            justify="center",

            font=Fonts.BODY,

            text_color=Colors.TEXT_SECONDARY,

            wraplength=320

        )

        description.grid(
            row=3,
            column=0,
            pady=(8,0)
        )