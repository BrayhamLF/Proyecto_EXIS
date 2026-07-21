"""
base_panel.py
--------------

Panel reutilizable.
"""

from __future__ import annotations

from components.core.base_component import BaseComponent
from config.theme.theme_manager import ThemeManager


class BasePanel(BaseComponent):

    def __init__(
        self,
        master,
        **kwargs
    ):

        super().__init__(master, fg_color=ThemeManager.current().SURFACE, **kwargs)

    def configure_grid(self):

        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=1)
