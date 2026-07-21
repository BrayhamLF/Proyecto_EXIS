"""Caso de uso de autenticación.

La validación contra MariaDB se conectará aquí cuando la infraestructura esté
lista. La interfaz nunca debe conocer esa implementación.
"""

from __future__ import annotations

from app.session import Session


class AuthService:
    """Crea la sesión para el flujo de acceso actual de la interfaz."""

    def authenticate(self, email: str, password: str, role: str) -> Session:
        normalized_email = email.strip().lower()
        normalized_role = role.strip()

        if not normalized_email or not password.strip() or not normalized_role:
            raise ValueError("Las credenciales y el rol son obligatorios.")

        display_name = normalized_email.split("@", maxsplit=1)[0].replace(".", " ")
        return Session(
            email=normalized_email,
            name=display_name.title(),
            role=normalized_role,
        )
