"""
navigation_button.py
--------------------

Botón de navegación reutilizable del sistema.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts
from config.sizes import Sizes


class NavigationButton(ctk.CTkFrame):

    HEIGHT = 48

    def __init__(
        self,
        master,
        text: str,
        icon=None,
        command=None
    ):

        super().__init__(
            master,
            fg_color="transparent",
            height=self.HEIGHT
        )

        self.command = command
        self.selected = False

        self.grid_columnconfigure(1, weight=1)
        self.grid_propagate(False)

        # ==========================================
        # Indicador lateral
        # ==========================================

        self.indicator = ctk.CTkFrame(
            self,
            width=4,
            fg_color="transparent",
            corner_radius=2
        )

        self.indicator.grid(
            row=0,
            column=0,
            sticky="ns",
            padx=(0, 8)
        )

        # ==========================================
        # Botón principal
        # ==========================================

        self.button = ctk.CTkButton(
            self,

            text=text,
            image=icon,

            anchor="w",
            compound="left",

            height=self.HEIGHT,

            fg_color="transparent",
            hover_color=Colors.PRIMARY_LIGHT,

            text_color=Colors.TEXT_WHITE,

            font=Fonts.BODY,

            corner_radius=Sizes.SMALL_RADIUS,

            border_width=0,

            command=self._on_click
        )

        self.button.grid(
            row=0,
            column=1,
            sticky="ew"
        )

    # ==================================================
    # Eventos
    # ==================================================

    def _on_click(self):

        if self.command:

            self.command()

    # ==================================================
    # Estados
    # ==================================================

    def select(self):

        self.selected = True

        self.indicator.configure(
            fg_color=Colors.SECONDARY
        )

        self.button.configure(
            fg_color=Colors.PRIMARY_DARK,
            hover_color=Colors.PRIMARY_DARK,
            text_color=Colors.TEXT_WHITE
        )

    def deselect(self):

        self.selected = False

        self.indicator.configure(
            fg_color="transparent"
        )

        self.button.configure(
            fg_color="transparent",
            hover_color=Colors.PRIMARY_LIGHT,
            text_color=Colors.TEXT_WHITE
        )

    # ==================================================
    # API
    # ==================================================

    def set_text(self, text: str):

        self.button.configure(text=text)

    def set_icon(self, icon):

        self.button.configure(image=icon)

    def enable(self):

        self.button.configure(state="normal")

    def disable(self):

        self.button.configure(state="disabled")