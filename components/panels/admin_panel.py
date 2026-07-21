"""
admin_panel.py
--------------

Panel base reutilizable para todas las secciones del Dashboard.
"""

from __future__ import annotations

import customtkinter as ctk

from components.dashboard.widgets.empty_state import EmptyState

from config.colors import Colors
from config.fonts import Fonts
from config.sizes import Sizes


class AdminPanel(ctk.CTkFrame):

    def __init__(
        self,
        master,
        title: str,
        height: int = 320,
        badge: int | str | None = None,
    ):

        super().__init__(
            master,
            height=height,
            fg_color=Colors.SURFACE,
            corner_radius=Sizes.LARGE_RADIUS,
            border_width=1,
            border_color=Colors.BORDER,
        )

        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.body = None
        self.badge = None
        self.empty_state = None

        # Build the base header/body first using a private base builder to
        # avoid calling an overridden _build implementation in subclasses.
        self._build_base(title, badge)

    # =====================================================
    # Construcción
    # =====================================================

    def _build_base(
        self,
        title,
        badge
    ):

        header = ctk.CTkFrame(

            self,

            height=60,

            fg_color=Colors.PRIMARY,

            corner_radius=Sizes.LARGE_RADIUS

        )

        header.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        header.grid_propagate(False)

        title_label = ctk.CTkLabel(

            header,

            text=title,

            font=Fonts.H3,

            text_color=Colors.TEXT_WHITE

        )

        title_label.pack(
            side="left",
            padx=(20,10),
            pady=18
        )

        if badge is not None:

            self.badge = ctk.CTkLabel(

                header,

                width=28,

                height=28,

                text=str(badge),

                corner_radius=14,

                fg_color=Colors.SECONDARY,

                text_color=Colors.TEXT_WHITE,

                font=Fonts.SMALL_BOLD

            )

            self.badge.pack(
                side="left"
            )

        self.body = ctk.CTkFrame(

            self,

            fg_color="transparent"

        )

        self.body.grid(

            row=1,

            column=0,

            sticky="nsew",

            padx=20,

            pady=18

        )

        self.body.grid_rowconfigure(0, weight=1)
        self.body.grid_columnconfigure(0, weight=1)

    # =====================================================
    # API
    # =====================================================

    def get_body(self):

        return self.body

    # -----------------------------------------------------

    def set_badge(self, value):

        if self.badge:

            self.badge.configure(
                text=str(value)
            )

    # -----------------------------------------------------

    def show_empty(
        self,
        icon,
        title,
        description
    ):

        self.hide_empty()

        self.empty_state = EmptyState(

            self.body,

            icon=icon,

            title=title,

            description=description

        )

        self.empty_state.grid(

            row=0,

            column=0,

            sticky="nsew"

        )

    # -----------------------------------------------------

    def hide_empty(self):

        if self.empty_state:

            self.empty_state.destroy()

            self.empty_state = None

    # -----------------------------------------------------

    def clear_body(self):

        self.hide_empty()

        for widget in self.body.winfo_children():

            widget.destroy()