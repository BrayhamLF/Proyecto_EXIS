"""
recent_activity_section.py
--------------------------

Actividad reciente del sistema.
"""

from __future__ import annotations

from components.panels.admin_panel import AdminPanel

from components.lists.list import List
from components.lists.activity_item import ActivityItem

from utils.icons import Icons

from config.colors import Colors


class RecentActivitySection(AdminPanel):

    def __init__(self, master):

        super().__init__(
            master,
            title="Actividad reciente",
            badge="0",
            height=320
        )

        self.activities = []

        self.activity_list = None

        self._build()

        self._load_demo()

    # ==================================================

    def _build(self):

        body = self.get_body()

        body.grid_rowconfigure(0, weight=1)
        body.grid_columnconfigure(0, weight=1)

        self.activity_list = List(body)

        self.activity_list.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

    # ==================================================

    def _load_demo(self):

        self.activities = [

            {

                "title":"Nuevo estudiante",

                "description":"Juan Pérez fue registrado",

                "time":"Hace 2 minutos",

                "icon":Icons.students((18,18)),

                "color":Colors.PRIMARY

            },

            {

                "title":"Monitor asignado",

                "description":"Programación II",

                "time":"Hace 18 minutos",

                "icon":Icons.monitors((18,18)),

                "color":Colors.SUCCESS

            },

            {

                "title":"Tutor creado",

                "description":"Carlos Rodríguez",

                "time":"Hace 1 hora",

                "icon":Icons.tutors((18,18)),

                "color":Colors.SECONDARY

            },

            {

                "title":"Espacio reservado",

                "description":"Sala 203",

                "time":"Hace 2 horas",

                "icon":Icons.spaces((18,18)),

                "color":Colors.ACCENT

            }

        ]

        self.refresh()

    # ==================================================

    def set_activities(self, activities):

        self.activities = activities

        self.refresh()

    # ==================================================

    def refresh(self):

        self.set_badge(len(self.activities))

        self.activity_list.clear()

        if not self.activities:

            self.activity_list.grid_remove()

            self.show_empty(

                icon=Icons.notification((48,48)),

                title="Sin actividad",

                description="No existen movimientos recientes."

            )

            return

        self.hide_empty()

        self.activity_list.grid()

        for activity in self.activities:

            self.activity_list.add_item(

                ActivityItem(

                    self.activity_list,

                    title=activity["title"],

                    description=activity["description"],

                    time=activity["time"],

                    icon=activity["icon"],

                    color=activity["color"]

                )

            )