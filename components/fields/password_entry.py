"""
password_entry.py
-----------------

Campo especializado para contraseña.
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
        # Reorganizar el grid para colocar el botón
        # dentro del mismo renglón del Entry.
        # --------------------------------------------------

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        # El Entry solo ocupa la primera columna
        self.entry.grid_forget()

        self.entry.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        # --------------------------------------------------
        # Botón mostrar/ocultar
        # --------------------------------------------------

        self.toggle_button = ctk.CTkButton(
            self,
            text="Mostrar",
            width=75,
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
    # Mostrar / Ocultar contraseña
    # ==================================================

    def toggle_password(self):

        self._visible = not self._visible

        if self._visible:

            self.entry.configure(show="")

            self.toggle_button.configure(
                text="Ocultar"
            )

        else:

            self.entry.configure(show="●")

            self.toggle_button.configure(
                text="Mostrar"
            )

    # ==================================================
    # API
    # ==================================================

    def is_visible(self) -> bool:

        return self._visible