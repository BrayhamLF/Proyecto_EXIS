"""
divider.py
----------

Separador horizontal reutilizable.
"""

from __future__ import annotations

import customtkinter as ctk

from config.theme.login_style import LoginStyle


class Divider(ctk.CTkFrame):

    def __init__(
        self,
        master,
        padx=0,
        pady=(0, 0)
    ):

        super().__init__(
            master,
            fg_color=LoginStyle.DIVIDER,
            height=1,
            corner_radius=0
        )

        self.grid(
            sticky="ew",
            padx=padx,
            pady=pady
        )