"""
secondary_button.py
-------------------
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts
from config.sizes import Sizes


class SecondaryButton(ctk.CTkButton):

    def __init__(
        self,
        master,
        text,
        command=None,
        width=None
    ):

        button_config = {
            "text": text,
            "command": command,
            "height": Sizes.BUTTON_HEIGHT,
            "fg_color": "transparent",
            "hover_color": Colors.LIGHT,
            "text_color": Colors.PRIMARY,
            "border_width": 2,
            "border_color": Colors.PRIMARY,
            "corner_radius": Sizes.SMALL_RADIUS,
            "font": Fonts.BUTTON,
            "cursor": "hand2"
        }

        if width is not None:
            button_config["width"] = width

        super().__init__(master, **button_config)