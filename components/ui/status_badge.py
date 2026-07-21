"""
status_badge.py
"""

from __future__ import annotations

import customtkinter as ctk

from config.fonts import Fonts


class StatusBadge(ctk.CTkLabel):

    def __init__(

        self,

        master,

        text,

        fg_color,

        text_color

    ):

        super().__init__(

            master,

            text=text,

            width=90,

            height=28,

            corner_radius=14,

            fg_color=fg_color,

            text_color=text_color,

            font=Fonts.SMALL_BOLD

        )