"""
dashboard_section.py
--------------------

Clase base para todas las secciones
del Dashboard.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from components.panels.admin_panel import AdminPanel
from components.dashboard.widgets.empty_state import EmptyState


class DashboardSection(AdminPanel, ABC):

    def __init__(
        self,
        master,
        title,
        badge=None,
        height=320
    ):

        super().__init__(
            master,
            title=title,
            badge=badge,
            height=height
        )

    # ==================================================
    # Helpers
    # ==================================================

    def clear_body(self):

        body = self.get_body()

        for widget in body.winfo_children():
            widget.destroy()

    # --------------------------------------------------

    def show_empty_state(
        self,
        *,
        icon,
        title,
        description
    ):

        self.clear_body()

        empty = EmptyState(

            self.get_body(),

            icon=icon,

            title=title,

            description=description

        )

        empty.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        return empty

    # --------------------------------------------------

    def update_badge(self, value):

        self.set_badge(value)

    # ==================================================
    # API
    # ==================================================

    @abstractmethod
    def refresh(self):
        """
        Cada sección implementará su propia
        actualización.
        """
        pass