"""
subtitle_label.py
-----------------

Subtítulos reutilizables.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class SubtitleLabel(ctk.CTkLabel):

    def __init__(
        self,
        master,
        text
    ):

        super().__init__(
            master,
            text=text,
            font=Fonts.BODY,
            text_color=Colors.TEXT_SECONDARY,
            justify="left",
            anchor="w",
            wraplength=540
        )