"""
hero_section.py
---------------

Banner principal del Dashboard.
"""

from __future__ import annotations

import customtkinter as ctk

from components.cards.base_card import BaseCard
from components.cards.quick_action_card import QuickActionCard

from config.colors import Colors
from config.fonts import Fonts
from config.settings import Settings

from utils.image_loader import ImageLoader
from utils.icons import Icons


class HeroSection(BaseCard):

    HERO_HEIGHT = 285

    def __init__(self, master):

        super().__init__(
            master,
            height=self.HERO_HEIGHT
        )

        self.banner = None

        self._build()

    # =====================================================
    # Construcción
    # =====================================================

    def _build(self):

        self.content.grid_rowconfigure(0, weight=1)

        self.content.grid_columnconfigure(
            0,
            weight=6
        )

        self.content.grid_columnconfigure(
            1,
            weight=4
        )

        self._build_left()

        self._build_right()

    # =====================================================
    # Panel izquierdo
    # =====================================================

    def _build_left(self):

        left = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        left.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(34, 24),
            pady=28
        )

        # ------------------------
        # Saludo
        # ------------------------

        hello = ctk.CTkLabel(

            left,

            text="Hola, Administrador",

            font=Fonts.TITLE,

            text_color=Colors.PRIMARY

        )

        hello.pack(
            anchor="w"
        )

        # ------------------------
        # Título
        # ------------------------

        title = ctk.CTkLabel(

            left,

            justify="left",

            text=(
                "Bienvenido al Sistema de Gestión\n"
                "de Monitorías y Tutorías Académicas"
            ),

            font=Fonts.DISPLAY,

            text_color=Colors.TEXT

        )

        title.pack(
            anchor="w",
            pady=(12, 12)
        )

        # ------------------------
        # Descripción
        # ------------------------

        description = ctk.CTkLabel(

            left,

            justify="left",

            wraplength=700,

            font=Fonts.BODY,

            text_color=Colors.TEXT_SECONDARY,

            text=(
                "Administre estudiantes, tutores, monitores, "
                "espacios académicos, monitorías, tutorías, "
                "seguimiento institucional y reportes desde "
                "una única plataforma."
            )

        )

        description.pack(
            anchor="w"
        )

        # ------------------------
        # Separador
        # ------------------------

        separator = ctk.CTkFrame(

            left,

            height=1,

            fg_color=Colors.BORDER

        )

        separator.pack(
            fill="x",
            pady=(24,18)
        )

        # ------------------------
        # Acciones rápidas
        # ------------------------

        self._build_actions(left)

    # =====================================================
    # Acciones rápidas
    # =====================================================

    def _build_actions(self, parent):

        actions = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        actions.pack(
            anchor="w"
        )

        actions.grid_rowconfigure(0, weight=1)

        for column in range(4):

            actions.grid_columnconfigure(
                column,
                weight=1
            )

        quick_actions = [

            ("Estudiantes", Icons.students()),

            ("Tutores", Icons.tutors()),

            ("Monitores", Icons.monitors()),

            ("Espacios", Icons.spaces())

        ]

        for column, (text, icon) in enumerate(quick_actions):

            QuickActionCard(

                actions,

                text=text,

                icon=icon

            ).grid(

                row=0,

                column=column,

                padx=(0 if column == 0 else 10, 0),

                sticky="ew"

            )

    # =====================================================
    # Imagen
    # =====================================================

    def _build_right(self):

        right = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        right.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(20,34),
            pady=18
        )

        image = ImageLoader.load(

            Settings.IMAGES_PATH / "dashboard_banner.png",

            (440,250)

        )

        self.banner = ctk.CTkLabel(

            right,

            image=image,

            text=""

        )

        self.banner.image = image

        self.banner.pack(
            expand=True,
            anchor="center"
        )