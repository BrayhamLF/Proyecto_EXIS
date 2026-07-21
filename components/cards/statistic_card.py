"""
statistic_card.py
-----------------

Tarjeta de indicador del Dashboard.
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
        color=Colors.PRIMARY,
        trend=None
    ):

        super().__init__(
            master,
            height=145
        )

        self.color = color

        self.title = title
        self.value = value
        self.icon = icon
        self.trend = trend

        self._build()

    # ==================================================

    def _build(self):

        self.content.grid_columnconfigure(0, weight=1)

        # -----------------------------
        # Cabecera
        # -----------------------------

        header = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=18,
            pady=(16,8)
        )

        # círculo

        circle = ctk.CTkFrame(

            header,

            width=46,

            height=46,

            fg_color=self.color,

            corner_radius=23

        )

        circle.pack(
            side="left"
        )

        circle.pack_propagate(False)

        lbl_icon = ctk.CTkLabel(

            circle,

            image=self.icon,

            text=""

        )

        lbl_icon.pack(
            expand=True
        )

        # tendencia

        self.trend_label = ctk.CTkLabel(

            header,

            text=self.trend or "",

            font=Fonts.SMALL_BOLD,

            text_color=Colors.SUCCESS

        )

        self.trend_label.pack(
            side="right"
        )

        # -----------------------------
        # Valor
        # -----------------------------

        self.value_label = ctk.CTkLabel(

            self.content,

            text=self.value,

            font=Fonts.H1,

            text_color=Colors.TEXT

        )

        self.value_label.grid(

            row=1,

            column=0,

            sticky="w",

            padx=18,

            pady=(8,2)

        )

        # -----------------------------
        # Texto
        # -----------------------------

        self.title_label = ctk.CTkLabel(

            self.content,

            text=self.title,

            font=Fonts.BODY,

            text_color=Colors.TEXT_SECONDARY

        )

        self.title_label.grid(

            row=2,

            column=0,

            sticky="w",

            padx=18,

            pady=(0,16)

        )

    # ==================================================
    # API
    # ==================================================

    def set_value(self, value):

        self.value_label.configure(
            text=value
        )

    def set_title(self, title):

        self.title_label.configure(
            text=title
        )

    def set_trend(
        self,
        value,
        color=Colors.SUCCESS
    ):

        self.trend_label.configure(

            text=value,

            text_color=color

        )