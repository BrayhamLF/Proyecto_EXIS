"""
login_right_panel.py
--------------------

Panel derecho del Login.
"""

from __future__ import annotations

import customtkinter as ctk

from components.panels.panel import Panel
from views.auth.login_form import LoginForm

from config.colors import Colors
from config.spacing import Spacing


class LoginRightPanel(Panel):

    def __init__(
        self,
        master,
        login_callback=None
    ):

        super().__init__(
            master,
            fg_color=Colors.BACKGROUND
        )

        self.login_callback = login_callback

        self.form: LoginForm | None = None

        self._build()

    # ==================================================
    # Construcción
    # ==================================================

    def _build(self):

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Contenedor centrado

        container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        container.grid(
            row=0,
            column=0,
            sticky=""
        )

        container.grid_columnconfigure(0, weight=1)

        # Formulario

        self.form = LoginForm(
            container,
            login_callback=self.login_callback
        )

        self.form.grid(
            row=0,
            column=0,
            padx=Spacing.HUGE,
            pady=Spacing.HUGE,
            sticky="nsew"
        )

    # ==================================================
    # API pública
    # ==================================================

    def focus_first_field(self):

        if self.form:
            self.form.focus_first_field()

    def clear(self):

        if self.form:
            self.form.clear()