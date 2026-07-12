"""
Tarjeta para mostrar indicadores del sistema.
"""

from __future__ import annotations

import customtkinter as ctk

from components.cards.base_card import BaseCard

from config.colors import Colors
from config.fonts import Fonts


class StatisticCard(BaseCard):

    def __init__(
        self,
        master,
        title,
        value="0",
        icon=None,
        accent_color=None
    ):

        super().__init__(
            master,
            width=240,
            height=150
        )

        accent_color = accent_color or Colors.PRIMARY

        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_columnconfigure(1, weight=1)

        # Barra superior

        self.value = ctk.CTkLabel(
            self.content,
            text=value,
            width=80,
            anchor="e",
            font=Fonts.H1,
            text_color=accent_color
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=12,
            pady=(12,18)
        )

        # Icono

        self.icon = ctk.CTkLabel(
            self.content,
            image=icon,
            text=""
        )

        self.icon.grid(
            row=1,
            column=0,
            sticky="w",
            padx=(20,0)
        )

        # Valor

        self.value = ctk.CTkLabel(
            self.content,
            text=value,
            font=Fonts.H1,
            text_color=accent_color
        )

        self.value.grid(
            row=1,
            column=1,
            sticky="e",
            padx=(0,20)
        )

        # Título

        self.title = ctk.CTkLabel(
            self.content,
            text=title,
            font=Fonts.BODY_BOLD,
            text_color=Colors.TEXT
        )

        self.title.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="w",
            padx=20,
            pady=(18,15)
        )

    def set_value(self, value):

        self.value.configure(text=str(value))