"""
header_title.py
---------------

Componente encargado del título y subtítulo
del Header.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class HeaderTitle(ctk.CTkFrame):

    def __init__(
        self,
        master,
        title="Dashboard",
        subtitle=""
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text=title,
            font=Fonts.H2,
            text_color=Colors.TEXT,
            anchor="w"
        )

        self.title_label.grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.subtitle_label = ctk.CTkLabel(
            self,
            text=subtitle,
            font=Fonts.SMALL,
            text_color=Colors.TEXT_SECONDARY,
            anchor="w"
        )

        self.subtitle_label.grid(
            row=1,
            column=0,
            sticky="w",
            pady=(2, 0)
        )

    # =====================================================
    # API
    # =====================================================

    def set_title(self, title: str):

        self.title_label.configure(
            text=title
        )

    def set_subtitle(self, subtitle: str):

        self.subtitle_label.configure(
            text=subtitle
        )

    def set(
        self,
        title: str,
        subtitle: str = ""
    ):

        self.set_title(title)

        self.set_subtitle(subtitle)

    def get_title(self):

        return self.title_label.cget("text")

    def get_subtitle(self):

        return self.subtitle_label.cget("text")