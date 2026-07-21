"""
password_entry.py
-----------------

Campo especializado para contraseñas.
"""

from __future__ import annotations

import customtkinter as ctk

from components.fields.line_entry import LineEntry

from config.colors import Colors
from config.fonts import Fonts


class PasswordEntry(LineEntry):

    def __init__(
        self,
        master,
        label="Contraseña",
        placeholder="Ingrese su contraseña"
    ):

        super().__init__(
            master,
            label=label,
            placeholder=placeholder,
            show="●"
        )

        self._visible = False

        # --------------------------------------------------
        # Reorganizar Grid
        # --------------------------------------------------

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.entry.grid_forget()

        self.entry.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        # --------------------------------------------------
        # Botón Mostrar / Ocultar
        # --------------------------------------------------

        self.toggle_button = ctk.CTkButton(

            self,

            text="Mostrar",

            width=80,

            height=34,

            fg_color="transparent",

            hover_color=Colors.SURFACE_ALT,

            text_color=Colors.PRIMARY,

            border_width=0,

            corner_radius=8,

            font=Fonts.SMALL,

            command=self.toggle_password

        )

        self.toggle_button.grid(

            row=1,

            column=1,

            padx=(8, 0)

        )

    # ==================================================
    # Mostrar / Ocultar
    # ==================================================

    def toggle_password(self):

        self.set_visible(
            not self._visible
        )

    # --------------------------------------------------

    def set_visible(
        self,
        visible: bool
    ):

        self._visible = visible

        if visible:

            self.entry.configure(
                show=""
            )

            self.toggle_button.configure(
                text="Ocultar"
            )

        else:

            self.entry.configure(
                show="●"
            )

            self.toggle_button.configure(
                text="Mostrar"
            )

    # ==================================================
    # API
    # ==================================================

    def is_visible(self) -> bool:

        return self._visible

    # --------------------------------------------------

    def clear(self):

        self.entry.delete(
            0,
            "end"
        )

    # --------------------------------------------------

    def set(
        self,
        value: str
    ):

        self.clear()

        self.entry.insert(
            0,
            value
        )

    # --------------------------------------------------

    def focus(self):

        self.entry.focus_set()

    # --------------------------------------------------

    def validate(self) -> bool:

        return bool(
            self.get().strip()
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

    def enable(self):

        self.entry.configure(
            state="normal"
        )

    # --------------------------------------------------

    def disable(self):

        self.entry.configure(
            state="disabled"
        )