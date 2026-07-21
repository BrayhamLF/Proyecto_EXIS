"""
sidebar_menu.py
---------------

Administrador del menú lateral.
"""

from __future__ import annotations

import customtkinter as ctk

from components.layout.sidebar_section import SidebarSection

from config.navigation import ROLE_MENUS


class SidebarMenu(ctk.CTkScrollableFrame):

    def __init__(
        self,
        master,
        role="Administrador",
        callback=None
    ):

        super().__init__(
            master,
            fg_color="transparent",
            corner_radius=0
        )

        self.callback = callback

        self.role = role

        self.sections = []

        self.current_option = None

        self.load(role)

    # ==================================================

    def load(self, role):

        self.role = role

        for widget in self.winfo_children():
            widget.destroy()

        self.sections.clear()

        for section in ROLE_MENUS.get(role, []):

            section_widget = SidebarSection(
                self,
                title=section.title,
                items=section.items,
                callback=self._selected
            )

            section_widget.pack(
                fill="x",
                pady=(0,8)
            )

            self.sections.append(section_widget)

        if ROLE_MENUS.get(role):

            first = ROLE_MENUS[role][0].items[0]

            self.select(first.id)

    # ==================================================

    def _selected(self, option):

        self.select(option)

        if self.callback:

            self.callback(option)

    # ==================================================

    def select(self, option):

        self.current_option = option

        for section in self.sections:

            section.clear_selection()

            section.select(option)

    # ==================================================

    def collapse(self):

        for section in self.sections:

            section.collapse()

    # ==================================================

    def expand(self):

        for section in self.sections:

            section.expand()