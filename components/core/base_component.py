"""
base_component.py
-----------------

Clase base para todos los componentes visuales.
"""

from __future__ import annotations

import customtkinter as ctk

from config.theme.theme_manager import ThemeManager


class BaseComponent(ctk.CTkFrame):

    def __init__(
        self,
        master,
        fg_color="transparent",
        **kwargs
    ):

        super().__init__(
            master,
            fg_color=fg_color,
            **kwargs
        )

        self.theme = ThemeManager.current()

        self.configure_grid()

        self.build()

    # ============================================
    # Métodos para sobreescribir
    # ============================================

    def configure_grid(self):

        pass

    def build(self):

        pass

    # ============================================
    # Utilidades
    # ============================================

    def refresh_theme(self):

        self.theme = ThemeManager.current()