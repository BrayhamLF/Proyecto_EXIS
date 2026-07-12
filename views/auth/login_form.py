"""
login_form.py
-------------

Formulario de inicio de sesión.
"""

from __future__ import annotations

import customtkinter as ctk

from components.fields.line_entry import LineEntry
from components.fields.password_entry import PasswordEntry
from components.fields.combo_box import ComboBox
from components.buttons.primary_button import PrimaryButton
from components.labels.title_label import TitleLabel
from components.labels.subtitle_label import SubtitleLabel

from config.strings import Strings
from config.colors import Colors


class LoginForm(ctk.CTkFrame):

    def __init__(
        self,
        master,
        login_callback=None
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.login_callback = login_callback

        self.email: LineEntry | None = None
        self.password: PasswordEntry | None = None
        self.role: ComboBox | None = None
        self.login_button: PrimaryButton | None = None

        self._build()

    # ==================================================
    # Construcción
    # ==================================================

    def _build(self):

        self.grid_columnconfigure(0, weight=1)

        row = 0

        # --------------------------------------------
        # Encabezado
        # --------------------------------------------

        ctk.CTkFrame(
            self,
            fg_color=Colors.GOLD,
            height=2
        ).grid(
            row=row,
            column=0,
            sticky="ew",
            pady=(0, 12)
        )

        row += 1

        TitleLabel(
            self,
            text=Strings.LOGIN_TITLE
        ).grid(
            row=row,
            column=0,
            sticky="ew"
        )

        self.grid_columnconfigure(0, weight=1)

        row += 1

        ctk.CTkFrame(
            self,
            fg_color=Colors.GOLD,
            height=2
        ).grid(
            row=row,
            column=0,
            sticky="ew",
            pady=(12, 16)
        )

        row += 1

        SubtitleLabel(
            self,
            text=Strings.LOGIN_SUBTITLE
        ).grid(
            row=row,
            column=0,
            sticky="w",
            pady=(0, 40)
        )

        row += 1

        # --------------------------------------------
        # Correo
        # --------------------------------------------

        self.email = LineEntry(
            self,
            label=Strings.EMAIL,
            placeholder="correo@unitropico.edu.co"
        )

        self.email.grid(
            row=row,
            column=0,
            sticky="ew",
            pady=(0, 22)
        )

        row += 1

        # --------------------------------------------
        # Contraseña
        # --------------------------------------------

        self.password = PasswordEntry(
            self,
            label=Strings.PASSWORD
        )

        self.password.grid(
            row=row,
            column=0,
            sticky="ew",
            pady=(0, 22)
        )

        row += 1

        # --------------------------------------------
        # Rol
        # --------------------------------------------

        self.role = ComboBox(
            self,
            label=Strings.ROLE,
            values=Strings.ROLES,
            default_value=Strings.SELECT_ROLE
        )

        self.role.grid(
            row=row,
            column=0,
            sticky="ew",
            pady=(0, 35)
        )

        row += 1

        # --------------------------------------------
        # Botón
        # --------------------------------------------

        self.login_button = PrimaryButton(
            self,
            text=Strings.LOGIN_BUTTON,
            command=self.login
        )

        self.login_button.grid(
            row=row,
            column=0,
            sticky="ew"
        )

    # ==================================================
    # Validación
    # ==================================================

    def _clear_validation(self):

        if self.email:
            self.email.clear_error()

        if self.password:
            self.password.clear_error()

        if self.role:
            self.role.clear_error()

    # ==================================================
    # Login
    # ==================================================

    def login(self):

        self._clear_validation()

        email = self.email.get().strip()
        password = self.password.get().strip()
        role = self.role.get().strip()

        # --------------------------------------------
        # Validaciones
        # --------------------------------------------

        if not email:

            self.email.set_error()
            self.email.focus()

            return

        if not password:

            self.password.set_error()
            self.password.focus()

            return

        if role in ("", Strings.SELECT_ROLE):

            self.role.set_error()
            self.role.focus()

            return

        # --------------------------------------------
        # Callback
        # --------------------------------------------

        if self.login_callback:

            self.login_callback(
                email,
                password,
                role
            )

    # ==================================================
    # API pública
    # ==================================================

    def focus_first_field(self):

        if self.email:
            self.email.focus()

    def clear(self):

        if self.email:
            self.email.clear()

        if self.password:
            self.password.clear()

        if self.role:
            self.role.set(Strings.SELECT_ROLE)

        self._clear_validation()