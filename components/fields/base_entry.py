"""
base_entry.py
-------------

Entry base reutilizable para todo el sistema.
"""

from __future__ import annotations

import re
import customtkinter as ctk

from components.fields.base_field import BaseField

from config.colors import Colors
from config.fonts import Fonts


class BaseEntry(BaseField):

    EMAIL_PATTERN = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    def __init__(
        self,
        master,
        label="",
        placeholder="",
        show=None,
        required=False,
        helper_text=""
    ):

        super().__init__(
            master=master,
            label=label,
            required=required,
            helper_text=helper_text
        )

        self.entry = ctk.CTkEntry(
            self.control_container,
            placeholder_text=placeholder,
            show=show,
            border_width=0,
            fg_color="transparent",
            text_color=Colors.TEXT,
            font=Fonts.BODY
        )

        self.entry.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=12,
            pady=8
        )

        self.control = self.entry

        self.entry.bind(
            "<FocusIn>",
            self._focus_in
        )

        self.entry.bind(
            "<FocusOut>",
            self._focus_out
        )

    # =====================================================
    # API
    # =====================================================

    def get(self):

        return self.entry.get()

    def set(self, value):

        self.entry.delete(0, "end")
        self.entry.insert(0, value)

    def clear(self):

        self.entry.delete(0, "end")

    def focus(self):

        self.entry.focus_set()

    def configure_state(self, state):

        self.entry.configure(state=state)

    # =====================================================
    # Eventos
    # =====================================================

    def _focus_in(self, _):

        self.set_focus_state()

    def _focus_out(self, _):

        self.clear_state()

    # =====================================================
    # Validación base
    # =====================================================

    def validate(self):

        value = self.get().strip()

        if self.required and not value:

            self.show_error(
                "Este campo es obligatorio."
            )

            self.set_error_state()

            return False

        self.clear_message()
        self.clear_state()

        return True