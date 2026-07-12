"""
base_card.py
------------

Tarjeta base reutilizable para todo el sistema.

Características:
- Sombra simulada
- Borde configurable
- Esquinas redondeadas
- Contenedor interno reutilizable
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors


class BaseCard(ctk.CTkFrame):

    SHADOW_OFFSET = 4
    CORNER_RADIUS = 18
    BORDER_WIDTH = 1
    PADDING = 24

    def __init__(
        self,
        master,
        width=None,
        height=None,
        fg_color=None,
        border_color=None,
        corner_radius=None,
        **kwargs
    ):

        super().__init__(
            master,
            fg_color="transparent",
            **kwargs
        )

        self.card_color = fg_color or Colors.SURFACE
        self.border_color = border_color or "#DCE3EA"
        self.corner_radius = corner_radius or self.CORNER_RADIUS

        if width:
            self.configure(width=width)

        if height:
            self.configure(height=height)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._create_shadow()
        self._create_card()
        self._create_content()

    # =====================================================
    # Sombra
    # =====================================================

    def _create_shadow(self):

        self.shadow = ctk.CTkFrame(
            self,
            fg_color="#D9DEE5",
            corner_radius=self.corner_radius
        )

        self.shadow.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(self.SHADOW_OFFSET, 0),
            pady=(self.SHADOW_OFFSET, 0)
        )

    # =====================================================
    # Tarjeta
    # =====================================================

    def _create_card(self):

        self.card = ctk.CTkFrame(
            self,
            fg_color=self.card_color,
            border_width=self.BORDER_WIDTH,
            border_color=self.border_color,
            corner_radius=self.corner_radius
        )

        self.card.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.card.grid_rowconfigure(0, weight=1)
        self.card.grid_columnconfigure(0, weight=1)

    # =====================================================
    # Contenido
    # =====================================================

    def _create_content(self):

        self.content = ctk.CTkFrame(
            self.card,
            fg_color="transparent"
        )

        self.content.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=self.PADDING,
            pady=self.PADDING
        )

        self.content.grid_columnconfigure(0, weight=1)

    # =====================================================
    # API
    # =====================================================

    def get_container(self):

        return self.content

    def set_border_color(self, color):

        self.card.configure(
            border_color=color
        )

    def set_background(self, color):

        self.card.configure(
            fg_color=color
        )

    def set_shadow_color(self, color):

        self.shadow.configure(
            fg_color=color
        )
