"""
list.py
--------

Contenedor reutilizable para listas del sistema.
"""

from __future__ import annotations

import customtkinter as ctk

from config.sizes import Sizes


class List(ctk.CTkScrollableFrame):

    ITEM_SPACING = Sizes.LIST_ITEM_SPACING

    def __init__(
        self,
        master,
        **kwargs
    ):

        super().__init__(

            master,

            fg_color="transparent",

            corner_radius=0,

            **kwargs

        )

        self.grid_columnconfigure(

            0,

            weight=1

        )

        self.items = []

    # ==================================================
    # API
    # ==================================================

    def add_item(self, item):

        item.pack(

            fill="x",

            pady=(0, self.ITEM_SPACING)

        )

        self.items.append(item)

    # --------------------------------------------------

    def add_items(self, items):

        for item in items:

            self.add_item(item)

    # --------------------------------------------------

    def remove_item(self, item):

        if item in self.items:

            self.items.remove(item)

            item.destroy()

    # --------------------------------------------------

    def clear(self):

        for item in self.items:

            item.destroy()

        self.items.clear()

    # --------------------------------------------------

    def count(self):

        return len(self.items)

    # --------------------------------------------------

    def is_empty(self):

        return len(self.items) == 0

    # --------------------------------------------------

    def get_items(self):

        return self.items

    # --------------------------------------------------

    def set_items(self, items):

        self.clear()

        self.add_items(items)