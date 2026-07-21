"""
icon_circle.py
--------------

Círculo institucional para mostrar iconos.
"""

from __future__ import annotations

import customtkinter as ctk


class IconCircle(ctk.CTkFrame):

    def __init__(
        self,
        master,
        image=None,
        size=46,
        color="#1E8E5A"
    ):

        super().__init__(

            master,

            width=size,

            height=size,

            fg_color=color,

            corner_radius=size//2

        )

        self.pack_propagate(False)

        label = ctk.CTkLabel(

            self,

            image=image,

            text=""

        )

        label.pack(expand=True)