"""
split_layout.py
---------------

Layout dividido.
"""

from __future__ import annotations

import customtkinter as ctk

from components.core.base_component import BaseComponent


class SplitLayout(BaseComponent):

    def __init__(

        self,

        master,

        left_weight=3,

        right_weight=7,

        **kwargs

    ):

        self.left_weight = left_weight

        self.right_weight = right_weight

        super().__init__(master, **kwargs)

    def configure_grid(self):

        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(
            0,
            weight=self.left_weight
        )

        self.grid_columnconfigure(
            1,
            weight=self.right_weight
        )

    def build(self):

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