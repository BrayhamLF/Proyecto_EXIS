"""
settings_tabs.py
----------------

Barra de navegación del módulo Configuración.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts
from config.sizes import Sizes


class SettingsTabs(ctk.CTkFrame):

    TAB_HEIGHT = 46

    def __init__(
        self,
        master,
        callback=None
    ):

        super().__init__(
            master,
            fg_color=Colors.SURFACE_ALT,
            corner_radius=Sizes.MEDIUM_RADIUS
        )

        self.callback = callback

        self.buttons = {}

        self.selected = "password"

        self.grid_columnconfigure(0, weight=1)

        self._build()

    # ==================================================
    # Construcción
    # ==================================================

    def _build(self):

        self.password_button = ctk.CTkButton(

            self,

            text="Cambio de contraseña",

            height=self.TAB_HEIGHT,

            corner_radius=Sizes.SMALL_RADIUS,

            fg_color=Colors.PRIMARY,

            hover_color=Colors.PRIMARY_DARK,

            text_color=Colors.TEXT_WHITE,

            font=Fonts.BODY_BOLD,

            command=lambda: self.select("password")

        )

        self.password_button.grid(

            row=0,

            column=0,

            padx=8,

            pady=8

        )

        self.buttons["password"] = self.password_button

    # ==================================================
    # API
    # ==================================================

    def select(self, option):

        if option == self.selected:
            return

        self.selected = option

        for key, button in self.buttons.items():

            if key == option:

                button.configure(

                    fg_color=Colors.PRIMARY,

                    text_color=Colors.TEXT_WHITE

                )

            else:

                button.configure(

                    fg_color=Colors.TRANSPARENT,

                    text_color=Colors.TEXT

                )

        if callable(self.callback):

            self.callback(option)