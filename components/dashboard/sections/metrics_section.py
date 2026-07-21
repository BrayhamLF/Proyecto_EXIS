"""
metrics_section.py
------------------

Sección de indicadores del Dashboard.
"""

from __future__ import annotations

import customtkinter as ctk

from components.cards.statistic_card import StatisticCard

from utils.icons import Icons

from config.colors import Colors


class MetricsSection(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self._build()

    # ==================================================
    # Construcción
    # ==================================================

    def _build(self):

        cards = [

            {
                "title": "Estudiantes",
                "value": "245",
                "trend": "+12",
                "icon": Icons.students((24,24)),
                "color": Colors.PRIMARY
            },

            {
                "title": "Tutores",
                "value": "18",
                "trend": "+2",
                "icon": Icons.tutors((24,24)),
                "color": Colors.SECONDARY
            },

            {
                "title": "Monitores",
                "value": "42",
                "trend": "+5",
                "icon": Icons.monitors((24,24)),
                "color": Colors.SUCCESS
            },

            {
                "title": "Espacios",
                "value": "12",
                "trend": "100%",
                "icon": Icons.spaces((24,24)),
                "color": Colors.ACCENT
            }

        ]

        for column, card in enumerate(cards):

            widget = StatisticCard(

                self,

                title=card["title"],

                value=card["value"],

                trend=card["trend"],

                icon=card["icon"],

                color=card["color"]

            )

            widget.grid(

                row=0,

                column=column,

                padx=8,

                sticky="nsew"

            )