"""
logout_button.py
----------------

Botón institucional para cerrar sesión.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts

from utils.icons import Icons


class LogoutButton(ctk.CTkFrame):

    HEIGHT = 48

    def __init__(
        self,
        master,
        command=None
    ):

        super().__init__(

            master,

            height=self.HEIGHT,

            fg_color="transparent",

            corner_radius=10

        )

        self.command = command

        self.grid_propagate(False)

        self.grid_columnconfigure(1, weight=1)

        self._build()

        self._bind_events()

    # ================================================

    def _build(self):

        self.icon = ctk.CTkLabel(

            self,

            text="",

            image=Icons.logout((18,18))

        )

        self.icon.grid(

            row=0,

            column=0,

            padx=(15,10)

        )

        self.label = ctk.CTkLabel(

            self,

            text="Cerrar sesión",

            anchor="w",

            font=Fonts.BODY_BOLD,

            text_color=Colors.TEXT_WHITE

        )

        self.label.grid(

            row=0,

            column=1,

            sticky="w"

        )

    # ================================================

    def _bind_events(self):

        widgets = (

            self,

            self.icon,

            self.label

        )

        for widget in widgets:

            widget.bind("<Button-1>", self._click)

            widget.bind("<Enter>", self._hover_in)

            widget.bind("<Leave>", self._hover_out)

    # ================================================

    def _click(self, event=None):

        if callable(self.command):

            self.command()

    # ================================================

    def _hover_in(self, event=None):

        self.configure(

            fg_color=Colors.PRIMARY_LIGHT

        )

    def _hover_out(self, event=None):

        self.configure(

            fg_color="transparent"

        )