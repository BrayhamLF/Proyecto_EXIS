"""Navegación entre las vistas de primer nivel de la aplicación."""

from __future__ import annotations


class Router:
    """Monta una única vista raíz y destruye de forma segura la anterior."""

    def __init__(self, application):
        self.application = application
        self.current = None

    def navigate(self, page) -> None:
        self.clear()
        self.current = page
        self.current.pack(fill="both", expand=True)

    def clear(self) -> None:
        if self.current is not None:
            self.current.destroy()
            self.current = None