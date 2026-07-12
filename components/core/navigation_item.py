"""
navigation_item.py
------------------

Modelo que representa una opción del menú lateral.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class NavigationItem:
    """
    Representa un elemento de navegación.
    """

    id: str

    title: str

    icon: str

    enabled: bool = True