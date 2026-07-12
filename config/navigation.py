"""
navigation.py
-------------

Configuración del menú principal.
"""

from components.core.navigation_item import NavigationItem


MAIN_MENU = [

    NavigationItem(
        id="dashboard",
        title="Dashboard",
        icon="menu-puntos-vertical.svg"
    ),

    NavigationItem(
        id="students",
        title="Estudiantes",
        icon="usuario-graduado.svg"
    ),

    NavigationItem(
        id="tutors",
        title="Tutores",
        icon="usuario-leccion.svg"
    ),

    NavigationItem(
        id="monitors",
        title="Monitores",
        icon="usuario-pizarra.svg"
    ),

    NavigationItem(
        id="spaces",
        title="Espacios",
        icon="edificio.svg"
    ),

    NavigationItem(
        id="sessions",
        title="Monitorías",
        icon="calendario.svg"
    ),

    NavigationItem(
        id="tracking",
        title="Seguimiento",
        icon="editar.svg"
    ),

    NavigationItem(
        id="reports",
        title="Reportes",
        icon="libro-alt.svg"
    )
]