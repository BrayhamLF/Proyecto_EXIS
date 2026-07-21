"""
dashboard_layout.py
-------------------

Layout principal del Dashboard del Administrador.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors

from components.dashboard.sections.hero_section import HeroSection
from components.dashboard.sections.metrics_section import MetricsSection
from components.dashboard.sections.review_students_section import ReviewStudentsSection
from components.dashboard.sections.next_session_section import NextSessionSection
from components.dashboard.sections.available_sessions_section import AvailableSessionsSection
from components.dashboard.sections.recent_activity_section import RecentActivitySection


class DashboardLayout(ctk.CTkFrame):

    SECTION_SPACING = 22
    COLUMN_SPACING = 18

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=Colors.BACKGROUND
        )

        self.hero = None
        self.metrics = None

        self.review_students = None
        self.next_session = None

        self.available_sessions = None
        self.recent_activity = None

        self._configure_grid()
        self._build()

    # ==================================================
    # Grid
    # ==================================================

    def _configure_grid(self):

        self.grid_columnconfigure(
            0,
            weight=1,
            uniform="dashboard"
        )

        self.grid_columnconfigure(
            1,
            weight=1,
            uniform="dashboard"
        )

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

    # ==================================================
    # Construcción
    # ==================================================

    def _build(self):

        self._build_hero()

        self._build_metrics()

        self._build_left_column()

        self._build_right_column()

    # ==================================================
    # Hero
    # ==================================================

    def _build_hero(self):

        self.hero = HeroSection(self)

        self.hero.grid(

            row=0,

            column=0,

            columnspan=2,

            sticky="ew",

            pady=(0, self.SECTION_SPACING)

        )

    # ==================================================
    # Indicadores
    # ==================================================

    def _build_metrics(self):

        self.metrics = MetricsSection(self)

        self.metrics.grid(

            row=1,

            column=0,

            columnspan=2,

            sticky="ew",

            pady=(0, self.SECTION_SPACING)

        )

    # ==================================================
    # Columna izquierda
    # ==================================================

    def _build_left_column(self):

        self.review_students = ReviewStudentsSection(self)

        self.review_students.grid(

            row=2,

            column=0,

            sticky="nsew",

            padx=(0, self.COLUMN_SPACING // 2),

            pady=(0, self.SECTION_SPACING)

        )

        self.recent_activity = RecentActivitySection(self)

        self.recent_activity.grid(

            row=3,

            column=0,

            sticky="nsew",

            padx=(0, self.COLUMN_SPACING // 2)

        )

    # ==================================================
    # Columna derecha
    # ==================================================

    def _build_right_column(self):

        self.next_session = NextSessionSection(self)

        self.next_session.grid(

            row=2,

            column=1,

            sticky="nsew",

            padx=(self.COLUMN_SPACING // 2, 0),

            pady=(0, self.SECTION_SPACING)

        )

        self.available_sessions = AvailableSessionsSection(self)

        self.available_sessions.grid(

            row=3,

            column=1,

            sticky="nsew",

            padx=(self.COLUMN_SPACING // 2, 0)

        )