"""
base_page.py
------------

Clase base para todas las páginas del sistema.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors


class BasePage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=Colors.BACKGROUND
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # ==================================================
    # API PARA MAINLAYOUT
    # ==================================================

    def get_title(self) -> str:
        return ""

    def get_subtitle(self) -> str:
        return ""

    def on_show(self):
        """Se ejecuta cuando la página pasa a ser visible."""
        pass

    def on_hide(self):
        """Se ejecuta antes de ocultar la página."""
        pass

    def refresh(self):
        """Actualiza la información de la página."""
        pass