"""
system_status.py
----------------
"""

from __future__ import annotations

from components.dashboard.sections.dashboard_section import DashboardSection
from components.dashboard.widgets.status_indicator import StatusIndicator


class SystemStatus(DashboardSection):

    def __init__(self, master):

        super().__init__(
            master,
            title="Estado del sistema",
            subtitle="Servicios principales"
        )

        self._build_status()

    # =========================================

    def _build_status(self):

        StatusIndicator(
            self.body,
            "Base de datos",
            "Conectada"
        ).pack(
            fill="x",
            pady=8
        )

        StatusIndicator(
            self.body,
            "Servidor",
            "En línea"
        ).pack(
            fill="x",
            pady=8
        )

        StatusIndicator(
            self.body,
            "Sistema",
            "Operativo"
        ).pack(
            fill="x",
            pady=8
        )

        StatusIndicator(
            self.body,
            "Respaldo",
            "Actualizado"
        ).pack(
            fill="x",
            pady=8
        )