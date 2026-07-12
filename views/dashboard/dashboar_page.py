"""
dashboard_page.py
-----------------

Página principal del sistema.
"""

from __future__ import annotations

import customtkinter as ctk

from views.base_page import BasePage

from components.cards.base_card import BaseCard
from components.cards.statistic_card import StatisticCard

from utils.image_loader import ImageLoader

from config.settings import Settings
from config.colors import Colors
from config.fonts import Fonts
from config.sizes import Sizes


class DashboardPage(BasePage):

    def __init__(self, master):

        super().__init__(master)

        # =============================================
        # Datos (temporales hasta integrar MariaDB)
        # =============================================

        self.statistics = {
            "students": 245,
            "tutors": 18,
            "monitors": 42,
            "spaces": 12,
        }

        # Referencias a las tarjetas

        self.students_card = None
        self.tutors_card = None
        self.monitors_card = None
        self.spaces_card = None

        # Layout

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._build()
    
    # ==========================================================
    # API DEL MAINLAYOUT
    # ==========================================================

    def get_title(self):

        return "Dashboard"

    def get_subtitle(self):

        return "Panel principal del sistema"

    def refresh(self):

        """
        Se utilizará posteriormente para
        actualizar la información desde
        la base de datos.
        """

        self.set_statistics(self.statistics)

    def on_show(self):

        self.refresh()

    # ==========================================================
    # CONSTRUCCIÓN
    # ==========================================================

    def _build(self):

        self._build_welcome()

        self._build_statistics()

        self._build_bottom()

    # ==========================================================
    # BIENVENIDA
    # ==========================================================
    def _build_welcome(self):

        card = BaseCard(
            self,
            height=185
        )

        card.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=5,
            pady=(5, 20)
        )

        container = card.content

        container.grid_columnconfigure(0, weight=1)

        # =====================================================
        # Barra institucional
        # =====================================================

        header_bar = ctk.CTkFrame(
            container,
            height=8,
            fg_color=Colors.PRIMARY,
            corner_radius=6
        )

        header_bar.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=18,
            pady=(18, 20)
        )

        # =====================================================
        # Bienvenida
        # =====================================================

        title = ctk.CTkLabel(
            container,
            text="Bienvenido",
            font=Fonts.H2,
            text_color=Colors.PRIMARY
        )

        title.grid(
            row=1,
            column=0,
            sticky="w",
            padx=25
        )

        subtitle = ctk.CTkLabel(
            container,
            text="Sistema de Gestión de Monitorías y Tutorías Académicas",
            font=Fonts.H3,
            text_color=Colors.TEXT
        )

        subtitle.grid(
            row=2,
            column=0,
            sticky="w",
            padx=25,
            pady=(8, 5)
        )

        description = ctk.CTkLabel(
            container,
            justify="left",
            anchor="w",
            wraplength=900,
            font=Fonts.BODY,
            text_color=Colors.TEXT_SECONDARY,
            text=(
                "Administre estudiantes, tutores, monitores, monitorías, "
                "tutorías académicas, espacios físicos y el seguimiento "
                "institucional desde una única plataforma."
            )
        )

        description.grid(
            row=3,
            column=0,
            sticky="w",
            padx=25,
            pady=(8, 20)
        )

    # ==========================================================
    # INDICADORES
    # ==========================================================
    def _build_statistics(self):

        section = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        section.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=5,
            pady=(0, 20)
        )

        # Cuatro columnas iguales

        for column in range(4):

            section.grid_columnconfigure(
                column,
                weight=1,
                uniform="statistics"
            )

        statistics = [

            {
                "key": "students",
                "title": "Estudiantes",
                "icon": "students.png",
                "color": Colors.PRIMARY,
            },

            {
                "key": "tutors",
                "title": "Tutores",
                "icon": "tutors.png",
                "color": Colors.SECONDARY,
            },

            {
                "key": "monitors",
                "title": "Monitores",
                "icon": "monitors.png",
                "color": Colors.SUCCESS,
            },

            {
                "key": "spaces",
                "title": "Espacios",
                "icon": "spaces.png",
                "color": Colors.ACCENT,
            }

        ]

        cards = []

        for column, item in enumerate(statistics):

            icon = ImageLoader.load(
                f"{Settings.ICONS_PATH}{item['icon']}",
                Settings.STATISTIC_ICON_SIZE
            )

            card = StatisticCard(
                section,
                title=item["title"],
                value=self.statistics[item["key"]],
                icon=icon,
                accent_color=item["color"]
            )

            card.grid(
                row=0,
                column=column,
                padx=8,
                pady=(5, 10),
                sticky="nsew"
            )

            cards.append(card)

        (
            self.students_card,
            self.tutors_card,
            self.monitors_card,
            self.spaces_card
        ) = cards
    
    # ==========================================================
    # SECCIÓN INFERIOR
    # ==========================================================

    def _build_bottom(self):

        """
        Se implementará más adelante.
        """

        pass