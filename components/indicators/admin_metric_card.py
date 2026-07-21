"""
admin_metric_card.py
--------------------

Tarjeta KPI del Dashboard del Administrador.
"""

from __future__ import annotations

import customtkinter as ctk

from components.cards.base_card import BaseCard

from config.colors import Colors
from config.fonts import Fonts
from config.sizes import Sizes

from utils.icons import Icons


class AdminMetricCard(BaseCard):

    def __init__(
        self,
        master,
        title: str,
        value: int | str = 0,
        icon=None,
        color=None,
        command=None
    ):

        super().__init__(
            master,
            height=Sizes.DASHBOARD_CARD_HEIGHT,
            corner_radius=Sizes.DASHBOARD_CARD_RADIUS
        )

        self.command = command

        self.color = color or Colors.PRIMARY

        self.icon = icon

        self.arrow = Icons.arrow_right(
            (Sizes.DASHBOARD_ARROW_SIZE,
             Sizes.DASHBOARD_ARROW_SIZE)
        )

        self.title_text = title

        self.value_text = str(value)
      
        self._build()

        self._bind_events()
        
        self.enabled = True


    # ==========================================================
    # Construcción
    # ==========================================================

    def _build(self):

        body = self.content

        body.grid_rowconfigure(1, weight=1)
        body.grid_columnconfigure(1, weight=1)

        padding = Sizes.DASHBOARD_CARD_PADDING

        # -----------------------------------------
        # Icono
        # -----------------------------------------

        self.icon_label = ctk.CTkLabel(

            body,

            image=self.icon,

            text=""

        )

        self.icon_label.grid(

            row=0,

            column=0,

            padx=(padding, 10),

            pady=(padding, 8)

        )

        # -----------------------------------------
        # Título
        # -----------------------------------------

        self.title = ctk.CTkLabel(

            body,

            text=self.title_text,

            font=Fonts.BODY_BOLD,

            text_color=Colors.TEXT

        )

        self.title.grid(

            row=0,

            column=1,

            sticky="w",

            pady=(padding, 8)

        )

        # -----------------------------------------
        # Flecha
        # -----------------------------------------

        self.arrow_label = ctk.CTkLabel(

            body,

            image=self.arrow,

            text=""

        )

        self.arrow_label.grid(

            row=0,

            column=2,

            padx=(0, padding),

            pady=(padding, 8)

        )

        # -----------------------------------------
        # Valor
        # -----------------------------------------

        self.value = ctk.CTkLabel(

            body,

            text=self.value_text,

            font=Fonts.H1,

            text_color=self.color

        )

        self.value.grid(

            row=1,

            column=0,

            columnspan=3,

            sticky="sw",

            padx=padding,

            pady=(0, padding)

        )

    # ==========================================================
    # Eventos
    # ==========================================================

    def set_enabled(self, enabled: bool):

        self.enabled = enabled

        state = "normal" if enabled else "disabled"

        self.title.configure(state=state)

        self.value.configure(state=state)

        self.icon_label.configure(state=state)

        self.arrow_label.configure(state=state)
        
    
    def _bind_events(self):

        widgets = [

            self,

            self.content,

            self.icon_label,

            self.title,

            self.value,

            self.arrow_label

        ]

        for widget in widgets:

            self._bind_widget(widget)
    
    def _bind_widget(self, widget):

        widget.bind("<Enter>", self._on_enter)

        widget.bind("<Leave>", self._on_leave)

        widget.bind("<Button-1>", self._on_click)

    def _on_enter(self, event=None):

        self.configure(
            fg_color=Colors.CARD_HOVER,
            border_color=self.color
        )

        self.content.configure(
            fg_color=Colors.CARD_HOVER
        )

        self.configure(cursor="hand2")

    def _on_leave(self, event=None):

        self.configure(
            border_color=Colors.BORDER
        )

    def _on_click(self, event=None):

        if not self.enabled:
            return

        if callable(self.command):
            self.command()
    
    def update_data(
        self,
        *,
        title=None,
        value=None,
        color=None
    ):

        if title is not None:
            self.set_title(title)

        if value is not None:
            self.set_value(value)

        if color is not None:
            self.set_color(color)

    # ==========================================================
    # API
    # ==========================================================

    def set_value(self, value):

        self.value.configure(
            text=str(value)
        )

    def set_title(self, title):

        self.title.configure(
            text=title
        )

    def set_color(self, color):

        self.color = color

        self.value.configure(
            text_color=color
        )