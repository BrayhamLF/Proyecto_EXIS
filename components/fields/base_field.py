"""
base_field.py
-------------

Componente base para todos los campos del sistema.

Incluye:

- Etiqueta
- Contenedor
- Widget principal (Entry, ComboBox, etc.)
- Widget izquierdo
- Widget derecho
- Mensaje de ayuda / error
- Estados visuales
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class BaseField(ctk.CTkFrame):

    FIELD_HEIGHT = 48
    CORNER_RADIUS = 12
    BORDER_WIDTH = 1

    def __init__(
        self,
        master,
        label="",
        required=False,
        helper_text="",
        **kwargs
    ):

        super().__init__(
            master,
            fg_color="transparent",
            **kwargs
        )

        self.required = required

        self.grid_columnconfigure(0, weight=1)

        self.left_widget = None
        self.right_widget = None
        self.control = None

        self._build(label, helper_text)

    # =====================================================
    # Construcción
    # =====================================================

    def _build(
        self,
        label,
        helper_text
    ):

        # -----------------------------------------
        # Label
        # -----------------------------------------

        self.label = ctk.CTkLabel(
            self,
            text=label,
            font=Fonts.BODY_BOLD,
            text_color=Colors.TEXT
        )

        self.label.grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, 6)
        )

        # -----------------------------------------
        # Contenedor del control
        # -----------------------------------------

        self.control_container = ctk.CTkFrame(
            self,
            fg_color=Colors.SURFACE,
            corner_radius=self.CORNER_RADIUS,
            border_width=self.BORDER_WIDTH,
            border_color=Colors.SUCCESS,
            height=self.FIELD_HEIGHT
        )

        self.control_container.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.control_container.grid_columnconfigure(
            1,
            weight=1
        )

        # -----------------------------------------
        # Mensaje inferior
        # -----------------------------------------

        self.message = ctk.CTkLabel(
            self,
            text=helper_text,
            font=Fonts.SMALL,
            text_color=Colors.TEXT_SECONDARY,
            anchor="w"
        )

        self.message.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(5, 0)
        )

    # =====================================================
    # Widgets laterales
    # =====================================================

    def add_leading_widget(
        self,
        widget
    ):

        self.left_widget = widget

        widget.grid(
            row=0,
            column=0,
            padx=(12, 8)
        )

    def add_trailing_widget(
        self,
        widget
    ):

        self.right_widget = widget

        widget.grid(
            row=0,
            column=2,
            padx=(8, 12)
        )

    # =====================================================
    # Estados visuales
    # =====================================================

    def clear_state(self):

        self.control_container.configure(
            border_color=Colors.SUCCESS,
            border_width=1
        )

    def set_focus_state(self):

        self.control_container.configure(
            border_color=Colors.SUCCESS,
            border_width=2
        )

    def set_error_state(self):

        self.control_container.configure(
            border_color="#DC2626",
            border_width=2
        )

    def set_success_state(self):

        self.control_container.configure(
            border_color="#16A34A",
            border_width=2
        )

    # =====================================================
    # Mensajes
    # =====================================================

    def show_error(
        self,
        text
    ):

        self.message.configure(
            text=text,
            text_color="#DC2626"
        )

    def show_success(
        self,
        text
    ):

        self.message.configure(
            text=text,
            text_color="#16A34A"
        )

    def show_info(
        self,
        text
    ):

        self.message.configure(
            text=text,
            text_color=Colors.TEXT_SECONDARY
        )

    def clear_message(self):

        self.message.configure(
            text=""
        )