"""
password_section.py
-------------------

Sección para actualizar la contraseña del usuario.
"""

from __future__ import annotations

import customtkinter as ctk

from components.cards.base_card import BaseCard

from config.colors import Colors
from config.fonts import Fonts

from views.settings.forms.password_form import PasswordForm


class PasswordSection(BaseCard):

    PADDING_X = 40
    PADDING_Y = 30

    def __init__(self, master):

        super().__init__(
            master,
            propagate=True
        )

        self.form = None

        self._build()

    # ==================================================
    # Construcción
    # ==================================================

    def _build(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.content.grid_columnconfigure(0, weight=1)

        self.content.grid_rowconfigure(0, weight=0)
        self.content.grid_rowconfigure(1, weight=0)
        self.content.grid_rowconfigure(2, weight=1)

        self._build_header()

        self._build_form()

    # ==================================================
    # Encabezado
    # ==================================================

    def _build_header(self):

        header = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=self.PADDING_X,
            pady=(self.PADDING_Y,20)
        )

        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(

            header,

            text="Actualizar contraseña",

            font=Fonts.H2,

            text_color=Colors.PRIMARY,

            anchor="w"

        )

        title.grid(
            row=0,
            column=0,
            sticky="w"
        )

        subtitle = ctk.CTkLabel(

            header,

            text=(
                "Actualiza la contraseña de acceso de tu cuenta "
                "institucional. Después de actualizarla será necesario "
                "iniciar sesión nuevamente para aplicar el cambio."
            ),

            justify="left",

            wraplength=900,

            font=Fonts.BODY,

            text_color=Colors.TEXT_SECONDARY,

            anchor="w"

        )

        subtitle.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(8,0)
        )

        separator = ctk.CTkFrame(

            self.content,

            height=1,

            fg_color=Colors.BORDER

        )

        separator.grid(

            row=1,

            column=0,

            sticky="ew",

            padx=self.PADDING_X,

            pady=(0,10)

        )

    # ==================================================
    # Formulario
    # ==================================================

    def _build_form(self):

        container = ctk.CTkFrame(

            self.content,

            fg_color="transparent"

        )

        container.grid(

            row=2,

            column=0,

            sticky="nsew",

            padx=self.PADDING_X,

            pady=(10,20)

        )

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.form = PasswordForm(
            container
        )

        self.form.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

    # ==================================================
    # API
    # ==================================================

    def clear(self):

        self.form.clear()

    def get_values(self):

        return self.form.get_values()