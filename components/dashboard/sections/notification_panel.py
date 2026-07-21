"""
notification_panel.py
---------------------
"""

from __future__ import annotations

from components.dashboard.sections.dashboard_section import DashboardSection
from components.dashboard.widgets.notification_item import NotificationItem


class NotificationPanel(DashboardSection):

    def __init__(self, master):

        super().__init__(
            master,
            title="Notificaciones",
            subtitle="Eventos pendientes"
        )

        self._load_demo()

    # =========================================

    def _load_demo(self):

        notifications = [

            "5 usuarios pendientes de aprobación",

            "2 tutores requieren asignación",

            "3 espacios disponibles",

            "Existe una copia de seguridad pendiente"

        ]

        for item in notifications:

            NotificationItem(
                self.body,
                item
            ).pack(
                fill="x",
                pady=8
            )