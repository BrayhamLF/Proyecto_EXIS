from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors


class AuthCard(ctk.CTkFrame):

    def __init__(
        self,
        master
    ):

        super().__init__(
            master,
            fg_color="white",
            corner_radius=24,
            border_width=1,
            border_color="#E6E6E6"
        )

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self.content = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.content.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=40,
            pady=40
        )

        self.content.grid_columnconfigure(0, weight=1)