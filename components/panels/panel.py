"""
panel.py
--------

Panel base reutilizable para vistas (p. ej. pantalla de login).
Este módulo exporta la clase Panel que actúa como un contenedor simple
con un subcontenedor `content` donde las vistas pueden colocar sus widgets.
"""

from __future__ import annotations

import customtkinter as ctk


class Panel(ctk.CTkFrame):
    """Contenedor base para paneles.

    Proporciona un frame principal (self) y un frame interno
    `self.content` donde las vistas alojan su UI.
    """

    def __init__(self, master, fg_color="transparent", **kwargs):
        super().__init__(master, fg_color=fg_color, **kwargs)

        # Evitar que el frame cambie de tamaño según hijos
        try:
            self.grid_propagate(False)
        except Exception:
            # Algunos contextos no soportan grid_propagate; ignorar si falla
            pass

        # Configurar grid para que `content` expanda
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Contenedor interno que las vistas usarán como área de contenido
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=0, column=0, sticky="nsew")

    # Compatibilidad: permitir acceso a `get_body` / `get_content` si el código lo espera
    def get_body(self):
        return self.content

    def get_content(self):
        return self.content
