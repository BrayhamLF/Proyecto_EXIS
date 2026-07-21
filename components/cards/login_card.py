"""Tarjeta de acceso mantenida como composición de ``LoginForm``."""

from __future__ import annotations

from components.cards.base_card import BaseCard
from views.auth.login_form import LoginForm


class LoginCard(BaseCard):
    """Contenedor reutilizable para mostrar el formulario de inicio de sesión."""

    def __init__(self, master, width: int | None = None, login_callback=None):
        super().__init__(master, width=width, propagate=True)

        self.form = LoginForm(self.content, login_callback=login_callback)
        self.form.grid(row=0, column=0, sticky="nsew", padx=32, pady=32)

    def focus_first_field(self) -> None:
        self.form.focus_first_field()
