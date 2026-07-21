"""
available_sessions_section.py
-----------------------------

Panel de monitorías y tutorías disponibles.
"""

from __future__ import annotations

from components.panels.admin_panel import AdminPanel

from components.dashboard.widgets.empty_state import EmptyState

from components.lists.list import List
from components.lists.session_list_item import SessionListItem

from utils.icons import Icons


class AvailableSessionsSection(AdminPanel):

    def __init__(self, master):

        super().__init__(
            master,
            title="Monitorías disponibles",
            badge="0",
            height=320
        )

        self.sessions = []

        self.session_list = None
        self.empty_state = None

        self._build()

        self._load_demo()

    # ==========================================================
    # Construcción
    # ==========================================================

    def _build(self):

        body = self.get_body()

        body.grid_rowconfigure(0, weight=1)
        body.grid_columnconfigure(0, weight=1)

        self.session_list = List(body)

        self.session_list.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

    # ==========================================================
    # Datos temporales
    # ==========================================================

    def _load_demo(self):

        self.sessions = [

            {
                "subject": "Programación II",
                "monitor": "Laura Gómez",
                "date": "Hoy",
                "hour": "08:00",
                "status": "Disponible"
            },

            {
                "subject": "Física I",
                "monitor": "Juan Pérez",
                "date": "Mañana",
                "hour": "10:00",
                "status": "Disponible"
            },

            {
                "subject": "Bases de Datos",
                "monitor": "Andrés Ruiz",
                "date": "Viernes",
                "hour": "14:00",
                "status": "Próxima"
            }

        ]

        self.refresh()

    # ==========================================================
    # API
    # ==========================================================

    def set_sessions(
        self,
        sessions: list[dict]
    ):

        self.sessions = sessions

        self.refresh()

    # ==========================================================
    # Actualizar
    # ==========================================================

    def refresh(self):

        self.set_badge(len(self.sessions))

        self.session_list.clear()

        if not self.sessions:

            self.session_list.grid_remove()

            self.show_empty(

                icon=Icons.sessions((48,48)),

                title="Sin monitorías",

                description=(
                    "Actualmente no existen "
                    "monitorías programadas."
                )

            )

            return

        self.hide_empty()

        self.session_list.grid()

        for session in self.sessions:

            self.session_list.add_item(

                SessionListItem(

                    self.session_list,

                    subject=session["subject"],

                    monitor=session["monitor"],

                    date=session["date"],

                    hour=session["hour"],

                    status=session["status"]

                )

            )