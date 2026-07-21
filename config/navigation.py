"""
navigation.py
-------------

Configuración centralizada de navegación del sistema.
"""

from __future__ import annotations

from dataclasses import dataclass, field


# ==========================================================
# ITEM
# ==========================================================

@dataclass(frozen=True)
class NavigationItem:

    id: str
    title: str
    icon: str


# ==========================================================
# SECCIÓN
# ==========================================================

@dataclass(frozen=True)
class NavigationSection:

    title: str
    items: list[NavigationItem] = field(default_factory=list)


# ==========================================================
# ADMINISTRADOR
# ==========================================================

ADMIN_MENU = [

    NavigationSection(

        "PANEL",

        [

            NavigationItem(
                "dashboard",
                "Dashboard",
                "dashboard"
            ),

        ]
    ),

    NavigationSection(

        "GESTIÓN DE PERSONAS",

        [

            NavigationItem(
                "users",
                "Usuarios",
                "users"
            ),

            NavigationItem(
                "students",
                "Estudiantes",
                "students"
            ),

            NavigationItem(
                "tutors",
                "Tutores",
                "tutors"
            ),

            NavigationItem(
                "monitors",
                "Monitores",
                "monitors"
            ),

        ]
    ),

    NavigationSection(

        "SESIONES ACADÉMICAS",

        [

            NavigationItem(
                "tutorials",
                "Tutorías",
                "tutorials"
            ),

            NavigationItem(
                "sessions",
                "Monitorías",
                "sessions"
            ),

        ]
    ),

    NavigationSection(

        "GESTIÓN ACADÉMICA",

        [

            NavigationItem(
                "spaces",
                "Espacios",
                "spaces"
            ),

            NavigationItem(
                "tracking",
                "Seguimiento",
                "tracking"
            ),

        ]
    ),

    NavigationSection(

        "CONTROL",

        [

            NavigationItem(
                "reports",
                "Reportes",
                "reports"
            ),

            NavigationItem(
                "settings",
                "Configuración",
                "settings"
            ),

        ]
    ),

]


# ==========================================================
# COORDINADOR
# ==========================================================

COORDINATOR_MENU = ADMIN_MENU


# ==========================================================
# TUTOR
# ==========================================================

TUTOR_MENU = [

    NavigationSection(

        "PANEL",

        [

            NavigationItem(
                "dashboard",
                "Dashboard",
                "dashboard"
            ),

        ]
    ),

    NavigationSection(

        "TUTORÍAS",

        [

            NavigationItem(
                "tutorials",
                "Tutorías",
                "tutorials"
            ),

            NavigationItem(
                "tracking",
                "Seguimiento",
                "tracking"
            ),

        ]
    ),

]


# ==========================================================
# MONITOR
# ==========================================================

MONITOR_MENU = [

    NavigationSection(

        "PANEL",

        [

            NavigationItem(
                "dashboard",
                "Dashboard",
                "dashboard"
            ),

        ]
    ),

    NavigationSection(

        "MONITORÍAS",

        [

            NavigationItem(
                "sessions",
                "Monitorías",
                "sessions"
            ),

            NavigationItem(
                "tracking",
                "Seguimiento",
                "tracking"
            ),

        ]
    ),

]


# ==========================================================
# ESTUDIANTE
# ==========================================================

STUDENT_MENU = [

    NavigationSection(

        "PANEL",

        [

            NavigationItem(
                "dashboard",
                "Dashboard",
                "dashboard"
            ),

        ]
    ),

    NavigationSection(

        "MIS SESIONES",

        [

            NavigationItem(
                "sessions",
                "Mis monitorías",
                "sessions"
            ),

        ]
    ),

]


# ==========================================================
# MENÚ POR ROL
# ==========================================================

ROLE_MENUS = {

    "Administrador": ADMIN_MENU,

    "Coordinador": COORDINATOR_MENU,

    "Tutor": TUTOR_MENU,

    "Monitor": MONITOR_MENU,

    "Estudiante": STUDENT_MENU,

}