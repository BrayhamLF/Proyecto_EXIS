"""
settings_page.py
----------------

Página principal del módulo Configuración.
"""

from __future__ import annotations

from views.base_page import BasePage
from views.settings.settings_layout import SettingsLayout


class SettingsPage(BasePage):

    def __init__(self, master):

        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.layout = None

        self._build()

    # ==================================================
    # API MainLayout
    # ==================================================

    def get_title(self):

        return "Configuración"

    def get_subtitle(self):

        return "Ajustes de la cuenta institucional."

    def on_show(self):

        pass

    # ==================================================

    def _build(self):

        self.layout = SettingsLayout(self)

        self.layout.grid(
            row=0,
            column=0,
            sticky="nsew"
        )