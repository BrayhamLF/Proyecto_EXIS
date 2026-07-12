"""
primary_button.py
-----------------

Botón principal reutilizable del sistema.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts
from config.sizes import Sizes
from config.radius import Radius


class PrimaryButton(ctk.CTkButton):

    def __init__(
        self,
        master,
        text: str,
        command=None,
        width=None
    ):

        button_config = {
            "text": text,
            "command": command,
            "height": Sizes.BUTTON_HEIGHT,
            "corner_radius": Radius.MD,
            "fg_color": Colors.PRIMARY,
            "hover_color": Colors.PRIMARY_HOVER,
            "text_color": Colors.TEXT_WHITE,
            "font": Fonts.BUTTON,
            "border_width": 0,
            "cursor": "hand2"
        }

        if width is not None:
            button_config["width"] = width

        super().__init__(master, **button_config)

        self._default_text = text

    # ==================================================
    # API
    # ==================================================

    def set_text(self, text: str):

        self.configure(text=text)

    def reset_text(self):

        self.configure(text=self._default_text)

    def enable(self):

        self.configure(
            state="normal"
        )

    def disable(self):

        self.configure(
            state="disabled"
        )

    def start_loading(self):

        self.disable()

        self.configure(
            text="Cargando..."
        )

    def stop_loading(self):

        self.enable()

        self.reset_text()
