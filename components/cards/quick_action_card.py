"""
quick_action_card.py
--------------------

Tarjeta de acceso rápido del Dashboard.
"""

from __future__ import annotations

import customtkinter as ctk

from components.cards.base_card import BaseCard

from config.colors import Colors
from config.fonts import Fonts
from config.sizes import Sizes


class QuickActionCard(BaseCard):

    WIDTH = 170
    HEIGHT = 62

    def __init__(
        self,
        master,
        text="",
        icon=None,
        command=None
    ):

        super().__init__(
            master,
            width=self.WIDTH,
            height=self.HEIGHT,
            propagate=False
        )

        self.command = command

        self.icon_label = None
        self.title_label = None

        self._build(text, icon)
        self._bind_events()

    # ==================================================
    # Construcción
    # ==================================================

    def _build(
        self,
        text,
        icon
    ):

        self.content.grid_columnconfigure(1, weight=1)

        self.icon_label = ctk.CTkLabel(

            self.content,

            image=icon,

            text="",

            width=30

        )

        self.icon_label.grid(

            row=0,

            column=0,

            padx=(18, 12),

            pady=16

        )

        self.title_label = ctk.CTkLabel(

            self.content,

            text=text,

            anchor="w",

            font=Fonts.BODY_BOLD,

            text_color=Colors.TEXT

        )

        self.title_label.grid(

            row=0,

            column=1,

            sticky="w",

            padx=(0,18)

        )

    # ==================================================
    # Eventos
    # ==================================================

    def _bind_events(self):

        widgets = (

            self,

            self.content,

            self.icon_label,

            self.title_label

        )

        for widget in widgets:

            widget.bind("<Button-1>", self._click)

            widget.bind("<Enter>", self._hover_in)

            widget.bind("<Leave>", self._hover_out)

    # ==================================================

    def _click(self, event=None):

        if callable(self.command):

            self.command()

    # ==================================================

    def _hover_in(self, event=None):

        self.configure(

            fg_color=Colors.SURFACE_ALT,

            border_color=Colors.PRIMARY

        )

    def _hover_out(self, event=None):

        self.configure(

            fg_color=Colors.SURFACE,

            border_color=Colors.BORDER

        )

    # ==================================================
    # API
    # ==================================================

    def set_text(self, text):

        self.title_label.configure(
            text=text
        )

    def set_icon(self, icon):

        self.icon_label.configure(
            image=icon
        )

    def set_command(self, command):

        self.command = command