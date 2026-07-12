"""
login_page.py
-------------

Vista principal del Login.
"""

from __future__ import annotations

import customtkinter as ctk

from views.auth.login_left_panel import LoginLeftPanel
from views.auth.login_right_panel import LoginRightPanel

from config.colors import Colors


class LoginPage(ctk.CTkFrame):

    LEFT_WEIGHT = 3
    RIGHT_WEIGHT = 9

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

        self.left_panel: LoginLeftPanel | None = None
        self.right_panel: LoginRightPanel | None = None

        self._build()

    # ==================================================
    # Construcción
    # ==================================================

    def _build(self):

        self.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(
            0,
            weight=self.LEFT_WEIGHT
        )

        self.grid_columnconfigure(
            1,
            weight=self.RIGHT_WEIGHT
        )

        # ---------------------------------------
        # Panel izquierdo
        # ---------------------------------------

        self.left_panel = LoginLeftPanel(self)

        self.left_panel.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # ---------------------------------------
        # Panel derecho
        # ---------------------------------------

        self.right_panel = LoginRightPanel(
            self,
            login_callback=self.login_callback
        )

        self.right_panel.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        # Dar el foco al primer campo al iniciar

        self.after(
            150,
            self.focus_first_field
        )

    # ==================================================
    # API pública
    # ==================================================

    def focus_first_field(self):

        if self.right_panel:
            self.right_panel.focus_first_field()

    def clear(self):

        if self.right_panel:
            self.right_panel.clear()