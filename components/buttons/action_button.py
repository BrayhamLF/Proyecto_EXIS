"""
action_button.py
----------------

Botón institucional para acciones rápidas.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class ActionButton(ctk.CTkButton):

    def __init__(
        self,
        master,
        text,
        image=None,
        command=None,
        width=145
    ):

        super().__init__(

            master,

            text=text,

            image=image,

            compound="left",

            width=width,

            height=42,

            corner_radius=10,

            fg_color=Colors.PRIMARY,

            hover_color=Colors.PRIMARY_HOVER,

            text_color=Colors.WHITE,

            font=Fonts.BODY_BOLD,

            command=command
        )