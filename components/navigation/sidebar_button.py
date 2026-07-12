"""
sidebar_button.py
-----------------

Botón de navegación del Sidebar.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts
from config.sizes import Sizes


class SidebarButton(ctk.CTkFrame):

    def __init__(
        self,
        master,
        text: str,
        command=None,
        icon= "assets/icons/menu-puntos-vertical.svg"
    ):

        super().__init__(
            master,
            fg_color="transparent",
            corner_radius=0
        )

        self.command = command

        self.active = False

        self.grid_columnconfigure(1, weight=1)

        # Barra lateral

        self.indicator = ctk.CTkFrame(
            self,
            width=5,
            corner_radius=0,
            fg_color="transparent"
        )

        self.indicator.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        self.button = ctk.CTkButton(
            self,
            text=text,
            image=icon,
            compound="left",
            anchor="w",
            height=48,
            corner_radius=10,
            fg_color="transparent",
            hover_color=Colors.SIDEBAR_HOVER,
            text_color=Colors.WHITE,
            font=Fonts.BODY_BOLD,
            command=self._clicked
        )

        self.button.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=(10, 10)
        )

    def _clicked(self):

        if self.command:

            self.command()

    def set_active(self):

        self.active = True

        self.indicator.configure(
            fg_color=Colors.ACCENT
        )

        self.button.configure(
            fg_color=Colors.SIDEBAR_ACTIVE
        )

    def set_inactive(self):

        self.active = False

        self.indicator.configure(
            fg_color="transparent"
        )

        self.button.configure(
            fg_color="transparent"
        )