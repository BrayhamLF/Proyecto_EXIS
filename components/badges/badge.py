"""
badge.py
--------

Insignia reutilizable.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class Badge(ctk.CTkFrame):

    def __init__(
        self,
        master,
        text
    ):

        super().__init__(
            master,
            fg_color=Colors.PRIMARY,
            corner_radius=0
        )

        label = ctk.CTkLabel(
            self,
            text=text.upper(),
            font=Fonts.CAPTION,
            text_color=Colors.SECONDARY
        )

        label.pack(
            padx=14,
            pady=7
        )