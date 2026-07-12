"""
title_label.py
--------------

Título principal.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class TitleLabel(ctk.CTkLabel):

    def __init__(
        self,
        master,
        text
    ):

        super().__init__(
            master,
            text=text,
            font=Fonts.H1,
            text_color=Colors.PRIMARY,
            anchor="w"
        )