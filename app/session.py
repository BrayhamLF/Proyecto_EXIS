"""Modelo de la sesión activa de la aplicación."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Session:
    """Información mínima del usuario autenticado."""

    id: int | None = None
    name: str = ""
    lastname: str = ""
    email: str = ""
    role: str = ""
    photo: str | None = None

    @property
    def full_name(self) -> str:
        return " ".join(part for part in (self.name, self.lastname) if part)

    @property
    def is_authenticated(self) -> bool:
        return bool(self.email and self.role)

    def clear(self) -> None:
        self.id = None
        self.name = ""
        self.lastname = ""
        self.email = ""
        self.role = ""
        self.photo = None

    def logout(self) -> None:
        """Alias semántico para conservar la API existente."""
        self.clear()
