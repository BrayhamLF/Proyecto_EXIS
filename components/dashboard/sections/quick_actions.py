"""
quick_actions.py
"""

from __future__ import annotations

import customtkinter as ctk

from components.dashboard.sections.dashboard_section import DashboardSection
from components.cards.quick_action_card import QuickActionCard

from utils.icons import Icons


class QuickActions(DashboardSection):

    def __init__(self, master):

        super().__init__(
            master,
            title="Acciones rápidas",
            subtitle="Operaciones más utilizadas"
        )

        self._build_actions()

    def _build_actions(self):

        for i in range(3):
            self.body.grid_columnconfigure(i, weight=1)

        actions = [

            ("Registrar\nEstudiante", Icons.students((30,30))),

            ("Registrar\nTutor", Icons.tutors((30,30))),

            ("Registrar\nMonitor", Icons.monitors((30,30))),

            ("Asignar\nEspacio", Icons.spaces((30,30))),

            ("Gestionar\nUsuarios", Icons.users((30,30))),

            ("Ver\nReportes", Icons.reports((30,30)))

        ]

        for index, (text, icon) in enumerate(actions):

            row = index // 3
            col = index % 3

            QuickActionCard(

                self.body,

                text=text,

                icon=icon

            ).grid(

                row=row,

                column=col,

                padx=10,

                pady=10,

                sticky="nsew"
            )

