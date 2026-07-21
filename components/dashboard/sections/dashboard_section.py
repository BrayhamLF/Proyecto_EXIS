"""
dashboard_section.py
--------------------

Contenedor reutilizable para las secciones de los dashboards.
"""

from __future__ import annotations

import customtkinter as ctk

from components.cards.base_card import BaseCard

from config.colors import Colors
from config.fonts import Fonts
from config.sizes import Sizes


class DashboardSection(BaseCard):

    def __init__(
        self,
        master,
        title: str = "",
        subtitle: str = "",
        **kwargs
    ):

        super().__init__(
            master,
            **kwargs
        )

        self.title = title
        self.subtitle = subtitle

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.body = None

        self._build()

    # =====================================================
    # Construcción
    # =====================================================

    def _build(self):

        # -------------------------
        # Encabezado
        # -------------------------

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=Sizes.SPACE_24,
            pady=(Sizes.SPACE_20, Sizes.SPACE_16)
        )

        header.grid_columnconfigure(0, weight=1)

        # -------------------------
        # Título
        # -------------------------

        self.title_label = ctk.CTkLabel(
            header,
            text=self.title,
            font=Fonts.H3,
            text_color=Colors.TEXT
        )

        self.title_label.grid(
            row=0,
            column=0,
            sticky="w"
        )

        # -------------------------
        # Subtítulo
        # -------------------------

        if self.subtitle:

            self.subtitle_label = ctk.CTkLabel(
                header,
                text=self.subtitle,
                font=Fonts.SMALL,
                text_color=Colors.TEXT_SECONDARY
            )

            self.subtitle_label.grid(
                row=1,
                column=0,
                sticky="w",
                pady=(4, 0)
            )

        # -------------------------
        # Separador
        # -------------------------

        separator = ctk.CTkFrame(
            self,
            fg_color=Colors.BORDER_LIGHT,
            height=1
        )

        separator.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=Sizes.SPACE_24
        )

        # -------------------------
        # Contenido
        # -------------------------

        self.body = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.body.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=Sizes.SPACE_24,
            pady=Sizes.SPACE_20
        )

        self.body.grid_columnconfigure(0, weight=1)

    # =====================================================
    # API Pública
    # =====================================================

    def set_title(self, text: str):

        self.title_label.configure(text=text)

    def set_subtitle(self, text: str):

        if hasattr(self, "subtitle_label"):

            self.subtitle_label.configure(text=text)