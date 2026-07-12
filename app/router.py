"""
Router principal de la aplicación.
"""

from __future__ import annotations


class Router:

    def __init__(self, application):

        self.application = application

        self.current = None

    def navigate(self, page):

        if self.current:

            self.current.destroy()

        self.current = page

        self.current.pack(
            fill="both",
            expand=True
        )