"""
Estado global de la aplicación.
"""

from __future__ import annotations


class AppState:

    def __init__(self):

        self.current_user = None

        self.current_role = None

        self.current_view = None

        self.permissions = []

        self.theme = "light"

        self.connected = False

    # ==========================================

    def clear(self):

        self.current_user = None

        self.current_role = None

        self.current_view = None

        self.permissions.clear()

        self.connected = False