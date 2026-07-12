"""
Layout del módulo de autenticación.
"""

from __future__ import annotations

import customtkinter as ctk


class AuthLayout(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=5)

        self.grid_columnconfigure(1, weight=7)

        self.left = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.right = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.left.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.right.grid(
            row=0,
            column=1,
            sticky="nsew"
        )