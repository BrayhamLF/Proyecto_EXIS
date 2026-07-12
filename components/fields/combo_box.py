"""
combo_box.py
------------

ComboBox moderno reutilizable del sistema.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class ComboBox(ctk.CTkFrame):

    def __init__(
        self,
        master,
        label="",
        values=None,
        default_value=""
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        if values is None:
            values = []

        self._has_error = False

        self.grid_columnconfigure(0, weight=1)

        # =====================================
        # Etiqueta
        # =====================================

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
            pady=(0, 8)
        )

        # =====================================
        # ComboBox
        # =====================================

        self.combo = ctk.CTkComboBox(
            self,
            values=values,

            fg_color=Colors.SURFACE,
            border_color=Colors.BORDER,
            border_width=1,

            button_color=Colors.PRIMARY,
            button_hover_color=Colors.PRIMARY_DARK,

            dropdown_fg_color=Colors.SURFACE,
            dropdown_hover_color=Colors.PRIMARY_SOFT,
            dropdown_text_color=Colors.TEXT,

            text_color=Colors.TEXT,

            font=Fonts.BODY,

            height=42,

            corner_radius=8
        )

        self.combo.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        if default_value:
            self.combo.set(default_value)

        # =====================================
        # Línea inferior
        # =====================================

        self.line = ctk.CTkFrame(
            self,
            fg_color=Colors.BORDER,
            height=2,
            corner_radius=1
        )

        self.line.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(5, 0)
        )

        self.combo.bind("<FocusIn>", self._focus_in)
        self.combo.bind("<FocusOut>", self._focus_out)

    # =================================================

    def _focus_in(self, event):

        if not self._has_error:

            self.line.configure(
                fg_color=Colors.PRIMARY,
                height=3
            )

    def _focus_out(self, event):

        if not self._has_error:

            self.line.configure(
                fg_color=Colors.BORDER,
                height=2
            )

    # =================================================
    # API
    # =================================================

    def get(self):

        return self.combo.get()

    def set(self, value):

        self.combo.set(value)

    def focus(self):

        self.combo.focus_set()

    def configure_values(self, values):

        self.combo.configure(values=values)

    # =================================================
    # Estados
    # =================================================

    def set_error(self):

        self._has_error = True

        self.line.configure(
            fg_color=Colors.ERROR,
            height=3
        )

    def set_success(self):

        self._has_error = False

        self.line.configure(
            fg_color=Colors.SUCCESS,
            height=3
        )

    def clear_error(self):

        self._has_error = False

        self.line.configure(
            fg_color=Colors.BORDER,
            height=2
        )