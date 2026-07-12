"""
Sesión del usuario.
"""

from __future__ import annotations


class Session:

    def __init__(self):

        self.id = None

        self.name = ""

        self.lastname = ""

        self.email = ""

        self.role = ""

        self.photo = None

    @property
    def full_name(self):

        return f"{self.name} {self.lastname}"

    def logout(self):

        self.id = None

        self.name = ""

        self.lastname = ""

        self.email = ""

        self.role = ""

        self.photo = None