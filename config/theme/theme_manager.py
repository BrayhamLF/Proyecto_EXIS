"""
theme_manager.py
----------------

Administrador del tema activo.
"""

from config.theme.light_theme import LightTheme
from config.theme.dark_theme import DarkTheme


class ThemeManager:

    _theme = LightTheme

    @classmethod
    def current(cls):

        return cls._theme

    @classmethod
    def set_light(cls):

        cls._theme = LightTheme

    @classmethod
    def set_dark(cls):

        cls._theme = DarkTheme