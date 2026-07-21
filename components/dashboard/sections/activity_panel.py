"""
activity_panel.py
-----------------

Panel de actividad reciente.
"""

from __future__ import annotations

from components.dashboard.sections.dashboard_section import DashboardSection

from components.lists.list import List
from components.lists.activity_item import ActivityItem

from utils.icons import Icons


class ActivityPanel(DashboardSection):

    def __init__(self, master):

        super().__init__(
            master,
            title="Actividad reciente",
            subtitle="Últimos movimientos registrados"
        )

        self.activities = []

        self._load_demo()

    # ==================================================
    # Datos de demostración
    # ==================================================

    def _load_demo(self):

        self.activities = [

            {
                "title": "Nuevo estudiante registrado",
                "date": "Hace 2 minutos"
            },

            {
                "title": "Tutor asignado a Matemáticas",
                "date": "Hace 10 minutos"
            },

            {
                "title": "Espacio liberado",
                "date": "Hace 18 minutos"
            },

            {
                "title": "Monitor creado",
                "date": "Hace 1 hora"
            },

            {
                "title": "Credenciales generadas",
                "date": "Hace 2 horas"
            }

        ]

        self.refresh()

    # ==================================================
    # API
    # ==================================================

    def set_activities(self, activities):

        self.activities = activities

        self.refresh()

    # ==================================================
    # Construcción
    # ==================================================

    def refresh(self):

        self.clear_body()

        self.update_badge(len(self.activities))

        if not self.activities:

            self.show_empty_state(

                icon=Icons.notification((48, 48)),

                title="Sin actividad",

                description="No existen actividades recientes."

            )

            return

        activity_list = List(self.get_body())

        activity_list.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        for activity in self.activities:

            activity_list.add_item(

                ActivityItem(

                    activity_list,

                    title=activity["title"],

                    date=activity["date"],

                    icon=Icons.notification()

                )

            )