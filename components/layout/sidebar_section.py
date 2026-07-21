"""
sidebar_section.py
------------------

Sección reutilizable del Sidebar.
"""

from __future__ import annotations

import customtkinter as ctk

from components.buttons.sidebar_button import SidebarButton

from config.colors import Colors
from config.fonts import Fonts
from config.settings import Settings
from utils.icons import Icons


class SidebarSection(ctk.CTkFrame):

    def __init__(
        self,
        master,
        title: str,
        items: list,
        callback=None
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.callback = callback
        self.buttons = {}

        self.grid_columnconfigure(0, weight=1)

        # -----------------------------
        # Título
        # -----------------------------

        self.label = ctk.CTkLabel(
            self,
            text=title.upper(),
            font=("Segoe UI", 10, "bold"),
            text_color=Colors.SECONDARY
        )

        self.label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=8,
            pady=(14, 7)
        )

        # -----------------------------
        # Botones
        # -----------------------------

        row = 1

        for item in items:

            button = SidebarButton(
                self,
                text=item.title,
            icon=Icons.get(item.icon, Settings.ICON_SIZE),
                command=lambda i=item: self._clicked(i.id)
            )

            button.grid(
                row=row,
                column=0,
                sticky="ew",
                pady=2
            )

            self.buttons[item.id] = button

            row += 1

    # =====================================

    def _clicked(self, option):

        self.clear_selection()

        self.buttons[option].set_active()

        if self.callback:

            self.callback(option)

    # =====================================

    def clear_selection(self):

        for button in self.buttons.values():

            button.set_inactive()

    # =====================================

    def select(self, option):

        if option in self.buttons:

            self.buttons[option].set_active()

    # =====================================

    def collapse(self):

        self.label.grid_remove()

        for button in self.buttons.values():

            button.collapse()

    # =====================================

    def expand(self):

        self.label.grid()

        for button in self.buttons.values():

            button.expand()
