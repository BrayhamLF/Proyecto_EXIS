"""
base_page.py
------------

Clase base para todas las páginas.
"""

from __future__ import annotations

from components.core.base_component import BaseComponent


class BasePage(BaseComponent):

    def configure_grid(self):

        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=1)