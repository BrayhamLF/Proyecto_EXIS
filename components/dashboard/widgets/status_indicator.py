"""
status_indicator.py
-------------------

Indicador de estado reutilizable.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class StatusIndicator(ctk.CTkFrame):

    def __init__(
        self,
        master,
        title="",
        value="",
        color=None
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        if color is None:
            color = Colors.SUCCESS

        self.grid_columnconfigure(1, weight=1)

        self._build(
            title,
            value,
            color
        )

    # =========================================

    def _build(
        self,
        title,
        value,
        color
    ):

        dot = ctk.CTkFrame(
            self,
            width=14,
            height=14,
            fg_color=color,
            corner_radius=7
        )

        dot.grid(
            row=0,
            column=0,
            padx=(0,15)
        )

        dot.grid_propagate(False)

        text_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        text_frame.grid(
            row=0,
            column=1,
            sticky="ew"
        )

        ctk.CTkLabel(
            text_frame,
            text=title,
            font=Fonts.BODY_BOLD,
            text_color=Colors.TEXT
        ).pack(anchor="w")

        ctk.CTkLabel(
            text_frame,
            text=value,
            font=Fonts.SMALL,
            text_color=Colors.TEXT_SECONDARY
        ).pack(anchor="w")