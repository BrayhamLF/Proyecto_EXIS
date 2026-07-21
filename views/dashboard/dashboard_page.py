"""
dashboard_page.py
-----------------

Página principal del Dashboard.
"""

from __future__ import annotations

import customtkinter as ctk

from views.base_page import BasePage

from views.dashboard.administrator.dashboard import DashboardLayout

from config.colors import Colors


class DashboardPage(BasePage):

    def __init__(self, master):

        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.layout = None

        self._build()

    # ==========================================================
    # API DEL MAINLAYOUT
    # ==========================================================

    def get_title(self):

        return "Dashboard"

    def get_subtitle(self):

        return (
            "Panel principal del Sistema de Gestión "
            "de Monitorías y Tutorías Académicas"
        )

    def refresh(self):

        """
        Posteriormente actualizará los datos desde MariaDB.
        """
        pass

    def on_show(self):

        self.refresh()

    # ==========================================================
    # Construcción
    # ==========================================================

    def _build(self):

        self.layout = DashboardLayout(self)

        self.layout.grid(
            row=0,
            column=0,
            sticky="nsew"
        )