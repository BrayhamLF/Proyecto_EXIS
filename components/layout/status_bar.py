"""
status_bar.py
-------------

Barra de estado inferior.

Responsabilidad:
Mostrar información contextual del sistema.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class StatusBar(ctk.CTkFrame):

    def __init__(
        self,
        master,
        height: int = 34
    ):

        super().__init__(
            master,
            height=height,
            fg_color=Colors.CARD,
            corner_radius=0
        )

        self.grid_columnconfigure(0, weight=1)

        self.message = ctk.CTkLabel(
            self,
            text="Sistema listo.",
            anchor="w",
            font=Fonts.SMALL,
            text_color=Colors.TEXT_SECONDARY
        )

        self.message.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=6
        )

    # ==========================================
    # API
    # ==========================================

    def set_message(
        self,
        text: str
    ):

        self.message.configure(
            text=text
        )

    def clear(self):

        self.message.configure(
            text=""
        )