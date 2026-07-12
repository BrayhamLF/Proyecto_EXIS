"""
login_card.py
-------------

Tarjeta principal del inicio de sesión.
"""

from __future__ import annotations

import customtkinter as ctk

from components.cards.base_card import BaseCard
from components.fields.password_entry import PasswordEntry
from components.buttons.secondary_button import BaseButton

from utils.image_loader import ImageLoader

from config.colors import Colors
from config.fonts import Fonts
from config.settings import Settings


class LoginCard(BaseCard):

    def __init__(
        self,
        master,
        width=None,
        login_callback=None
    ):

        super().__init__(
            master,
            width=width or Settings.LOGIN_CARD_WIDTH
        )

        self.login_callback = login_callback

        self.logo = None

        self.email = None
        self.password = None
        self.role = None

        self.login_button = None

        self._build_content()

    # =====================================================
    # Construcción principal
    # =====================================================

    def _build_content(self):

        container = self.content

        container.grid_columnconfigure(0, weight=1)

        row = 0

        row = self._build_logo(container, row)
        row = self._build_header(container, row)
        row = self._build_separator(container, row)
        row = self._build_form(container, row)
        row = self._build_button(container, row)
        row = self._build_footer(container, row)

    # =====================================================
    # Logo
    # =====================================================

    def _build_logo(self, parent, row):

        self.logo = ImageLoader.load(
            Settings.LOGO_PATH,
            (170, 170)
        )

        logo = ctk.CTkLabel(
            parent,
            image=self.logo,
            text=""
        )

        logo.grid(
            row=row,
            column=0,
            pady=(10, 20)
        )

        return row + 1

    # =====================================================
    # Encabezado
    # =====================================================

    def _build_header(self, parent, row):

        title = ctk.CTkLabel(
            parent,
            text="Sistema de Gestión",
            font=Fonts.H2,
            text_color=Colors.TEXT
        )

        title.grid(
            row=row,
            column=0
        )

        subtitle = ctk.CTkLabel(
            parent,
            text="Monitorías y Tutorías Académicas",
            font=Fonts.BODY,
            text_color=Colors.TEXT_SECONDARY
        )

        subtitle.grid(
            row=row + 1,
            column=0,
            pady=(8, 4)
        )

        description = ctk.CTkLabel(
            parent,
            text="Ingrese sus credenciales institucionales",
            font=Fonts.SMALL,
            text_color=Colors.TEXT_SECONDARY
        )

        description.grid(
            row=row + 2,
            column=0,
            pady=(0, 20)
        )

        return row + 3

    # =====================================================
    # Separador
    # =====================================================

    def _build_separator(self, parent, row):

        separator = ctk.CTkFrame(
            parent,
            height=2,
            fg_color=Colors.PRIMARY
        )

        separator.grid(
            row=row,
            column=0,
            sticky="ew",
            padx=120,
            pady=(0, 30)
        )

        return row + 1

    # =====================================================
    # Formulario
    # =====================================================

    def _build_form(self, parent, row):

        form = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        form.grid(
            row=row,
            column=0,
            sticky="ew",
            padx=30
        )

        form.grid_columnconfigure(0, weight=1)

        self.password = PasswordEntry(form)

        self.password.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(0, 18)
        )

        return row + 1

    # =====================================================
    # Botón
    # =====================================================

    def _build_button(self, parent, row):

        self.login_button = BaseButton(
            parent,
            text="Iniciar sesión",
            command=self._login
        )

        self.login_button.grid(
            row=row,
            column=0,
            sticky="ew",
            padx=30,
            pady=(35, 20)
        )

        return row + 1

    # =====================================================
    # Footer
    # =====================================================

    def _build_footer(self, parent, row):

        footer = ctk.CTkLabel(
            parent,
            text="Universidad Internacional del Trópico Americano",
            font=Fonts.SMALL,
            text_color=Colors.TEXT_SECONDARY
        )

        footer.grid(
            row=row,
            column=0,
            pady=(0, 10)
        )

        return row + 1

    # =====================================================
    # Login
    # =====================================================

    def _login(self):

        ok = True

        ok &= self.email.validate()
        ok &= self.password.validate()
        ok &= self.role.validate()

        if not ok:
            return

        if self.login_callback:

            self.login_callback(
                self.email.get().strip(),
                self.password.get(),
                self.role.get()
            )

    # =====================================================
    # API
    # =====================================================

    def focus_first_field(self):

        self.email.focus()
