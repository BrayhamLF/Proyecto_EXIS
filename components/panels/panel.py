"""
panel.py
--------

Panel reutilizable.
"""

from __future__ import annotations

import customtkinter as ctk


class Panel(ctk.CTkFrame):

    def __init__(
        self,
        master,
        fg_color="transparent",
        corner_radius=0,
        **kwargs
    ):

        super().__init__(
            master,
            fg_color=fg_color,
            corner_radius=corner_radius,
            **kwargs
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.content = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.content.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.content.grid_columnconfigure(
            0,
            weight=1
        )
