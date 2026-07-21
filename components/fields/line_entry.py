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

    ENTRY_HEIGHT = 40
    LINE_HEIGHT = 2

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
        self._default_line_color = Colors.BORDER

        self._build_label(label)
        self._build_entry(placeholder, show)
        self._build_line()

        self.entry.bind("<FocusIn>", self._focus_in)
        self.entry.bind("<FocusOut>", self._focus_out)

    # ==================================================
    # Construcción
    # ==================================================

    def _build_label(self, text):

        self.label = ctk.CTkLabel(

            self,

            text=text,

            font=Fonts.BODY_BOLD,

            text_color=Colors.TEXT

        )

        self.label.grid(

            row=0,

            column=0,

            sticky="w",

            pady=(0, 8)

        )

    # --------------------------------------------------

    def _build_entry(
        self,
        placeholder,
        show
    ):

        self.entry = ctk.CTkEntry(

            self,

            placeholder_text=placeholder,

            show=show,

            height=self.ENTRY_HEIGHT,

            border_width=0,

            corner_radius=0,

            fg_color="transparent",

            text_color=Colors.TEXT,

            font=Fonts.BODY

        )

        self.entry.grid(

            row=1,

            column=0,

            sticky="ew"

        )

    # --------------------------------------------------

    def _build_line(self):

        self.line = ctk.CTkFrame(

            self,

            height=self.LINE_HEIGHT,

            fg_color=self._default_line_color,

            corner_radius=1

        )

        self.line.grid(

            row=2,

            column=0,

            sticky="ew",

            pady=(5, 0)

        )

    # ==================================================
    # Eventos
    # ==================================================

    def _focus_in(self, event=None):

        if self._has_error:
            return

        self.line.configure(

            fg_color=Colors.PRIMARY,

            height=3

        )

    # --------------------------------------------------

    def _focus_out(self, event=None):

        if self._has_error:
            return

        self.line.configure(

            fg_color=self._default_line_color,

            height=self.LINE_HEIGHT

        )

    # ==================================================
    # API
    # ==================================================

    def get(self):

        return self.entry.get()

    # --------------------------------------------------

    def set(self, value):

        self.clear()

        self.entry.insert(
            0,
            value
        )

    # --------------------------------------------------

    def clear(self):

        self.entry.delete(0, "end")

        self.clear_error()

    # --------------------------------------------------

    def focus(self):

        self.entry.focus_set()

    # --------------------------------------------------

    def validate(self):

        return bool(
            self.get().strip()
        )

    # --------------------------------------------------

    def is_empty(self):

        return not self.validate()

    # --------------------------------------------------

    def enable(self):

        self.entry.configure(
            state="normal"
        )

    # --------------------------------------------------

    def disable(self):

        self.entry.configure(
            state="disabled"
        )

    # --------------------------------------------------

    def configure_state(self, state):

        self.entry.configure(
            state=state
        )

    # --------------------------------------------------

    def set_readonly(
        self,
        readonly=True
    ):

        self.entry.configure(

            state="readonly" if readonly else "normal"

        )

    # --------------------------------------------------

    def bind(self, sequence, command):

        self.entry.bind(
            sequence,
            command
        )

    # --------------------------------------------------

    def get_entry(self):

        return self.entry

    # --------------------------------------------------

    def set_placeholder(self, text):

        self.entry.configure(
            placeholder_text=text
        )

    # --------------------------------------------------

    def set_label(self, text):

        self.label.configure(
            text=text
        )

    # ==================================================
    # Estados visuales
    # ==================================================

    def clear_error(self):

        self._has_error = False

        self.line.configure(

            fg_color=self._default_line_color,

            height=self.LINE_HEIGHT

        )

    # --------------------------------------------------

    def set_error(self):

        self._has_error = True

        self.line.configure(

            fg_color=Colors.ERROR,

            height=3

        )

    # --------------------------------------------------

    def set_success(self):

        self._has_error = False

        self.line.configure(

            fg_color=Colors.SUCCESS,

            height=3

        )

    # --------------------------------------------------

    def set_warning(self):

        self._has_error = False

        self.line.configure(

            fg_color=Colors.WARNING,

            height=3

        )

    # --------------------------------------------------

    def has_error(self):

        return self._has_error

    # --------------------------------------------------

    def length(self):

        return len(self.get())

    # --------------------------------------------------

    def select_all(self):

        self.entry.select_range(
            0,
            "end"
        )

        self.entry.icursor("end")