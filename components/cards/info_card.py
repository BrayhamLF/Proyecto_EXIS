"""
info_card.py
------------

Tarjeta informativa reutilizable.
"""

from __future__ import annotations

import customtkinter as ctk

from components.cards.base_card import BaseCard

from config.colors import Colors
from config.fonts import Fonts


class InfoCard(BaseCard):

    def __init__(
        self,
        master,
        title="",
        value="",
        subtitle="",
        icon=None
    ):

        super().__init__(
            master,
            height=140
        )

        self.grid_columnconfigure(1, weight=1)

        self.icon = icon

        self._build(
            title,
            value,
            subtitle
        )

    # =====================================

    def _build(
        self,
        title,
        value,
        subtitle
    ):

        # -------------------------
        # Icono
        # -------------------------

        if self.icon:

            ctk.CTkLabel(

                self,

                image=self.icon,

                text=""

            ).grid(

                row=0,

                column=0,

                rowspan=2,

                padx=20,

                pady=20

            )

        # -------------------------
        # Título
        # -------------------------

        self.title = ctk.CTkLabel(

            self,

            text=title,

            font=Fonts.SMALL,

            text_color=Colors.TEXT_SECONDARY

        )

        self.title.grid(

            row=0,

            column=1,

            sticky="sw",

            padx=(0,20),

            pady=(20,0)

        )

        # -------------------------
        # Valor
        # -------------------------

        self.value = ctk.CTkLabel(

            self,

            text=value,

            font=Fonts.H1,

            text_color=Colors.TEXT

        )

        self.value.grid(

            row=1,

            column=1,

            sticky="nw",

            padx=(0,20)

        )

        # -------------------------
        # Subtítulo
        # -------------------------

        self.subtitle = ctk.CTkLabel(

            self,

            text=subtitle,

            font=Fonts.SMALL,

            text_color=Colors.TEXT_SECONDARY

        )

        self.subtitle.grid(

            row=2,

            column=1,

            sticky="nw",

            padx=(0,20),

            pady=(0,20)

        )

    # =====================================

    def set_value(self, value):

        self.value.configure(text=value)

    def set_title(self, title):

        self.title.configure(text=title)

    def set_subtitle(self, subtitle):

        self.subtitle.configure(text=subtitle)