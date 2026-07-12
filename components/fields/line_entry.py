"""
line_entry.py
-------------

Campo de texto moderno con línea inferior.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class LineEntry(ctk.CTkFrame):

    def __init__(
        self,
        master,
        label="",
        placeholder="",
        show=None
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0, weight=1)

        self._has_error = False

        # ==========================================
        # Etiqueta
        # ==========================================

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

        # ==========================================
        # Entrada
        # ==========================================

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text=placeholder,
            show=show,
            border_width=0,
            fg_color="transparent",
            text_color=Colors.TEXT,
            font=Fonts.BODY,
            height=40
        )

        self.entry.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        # ==========================================
        # Línea inferior
        # ==========================================

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

        self.entry.bind("<FocusIn>", self._focus_in)
        self.entry.bind("<FocusOut>", self._focus_out)

    # ==================================================
    # Eventos
    # ==================================================

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

    # ==================================================
    # API
    # ==================================================

    def get(self):

        return self.entry.get()

    def set(self, value):

        self.clear()

        self.entry.insert(0, value)

    def clear(self):

        self.entry.delete(0, "end")

    def focus(self):

        self.entry.focus_set()

    def bind(self, sequence, command):

        self.entry.bind(sequence, command)

    def configure_state(self, state):

        self.entry.configure(state=state)

    def get_entry(self):

        return self.entry

    # ==================================================
    # Estados visuales
    # ==================================================

    def clear_error(self):

        self._has_error = False

        self.line.configure(
            fg_color=Colors.BORDER,
            height=2
        )

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