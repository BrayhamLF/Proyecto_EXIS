"""
colors.py
---------

Paleta oficial del Sistema de Gestión de
Monitorías y Tutorías Académicas.
"""


class Colors:

    # ==================================================
    # Identidad institucional
    # ==================================================

    PRIMARY = "#045C54"

    PRIMARY_HOVER = "#0A6B62"

    PRIMARY_DARK = "#034943"

    PRIMARY_LIGHT = "#538C86"

    PRIMARY_SOFT = "#72A49C"

    SECONDARY = "#B3A46C"

    SECONDARY_LIGHT = "#C8BA84"

    # Accent / secondary alias
    ACCENT = SECONDARY

    GOLD = "#D4AF37"

    # ==================================================
    # Fondos
    # ==================================================

    BACKGROUND = "#DBE5E0"

    SURFACE = "#FFFFFF"

    SURFACE_ALT = "#F4F7F5"

    # Alias para compatibilidad
    LIGHT = SURFACE_ALT

    WHITE = "#FFFFFF"

    BLACK = "#000000"

    # Alias tarjeta (compatibilidad)
    CARD = SURFACE

    # ==================================================
    # Bordes
    # ==================================================

    BORDER = "#C7D3CF"

    BORDER_FOCUS = PRIMARY

    BORDER_LIGHT = "#E6ECE9"

    # ==================================================
    # Sidebar
    # ==================================================

    SIDEBAR = PRIMARY

    SIDEBAR_HOVER = PRIMARY_HOVER

    # ==================================================
    # Texto
    # ==================================================

    TEXT = "#183530"

    TEXT_SECONDARY = "#5B7773"

    TEXT_LIGHT = "#91AAA5"

    TEXT_WHITE = "#FFFFFF"

    # ==================================================
    # Estados
    # ==================================================

    SUCCESS = "#3D8B5C"

    WARNING = "#D2A53B"

    ERROR = "#C94B4B"

    INFO = "#5D93B5"

    # ==================================================
    # Extras
    # ==================================================

    SHADOW = "#C7D1CC"

    OVERLAY = "#00000022"

    TRANSPARENT = "transparent"
    
    # ==================================================
    # Dashboard
    # ==================================================

    CARD_NORMAL = SURFACE

    CARD_HOVER = "#F7FAFC"

    CARD_BORDER = BORDER

    CARD_BORDER_ACTIVE = PRIMARY
   
    CARD_SHADOW = "#EEF2F7"

    SUCCESS_BG = "#EAF8EF"

    WARNING_BG = "#FFF8E5"

    ERROR_BG = "#FDECEC"

    PRIMARY_BG = "#EEF5FF"

    # Compatibility aliases (light variants used across components)
    SUCCESS_LIGHT = SUCCESS_BG
    WARNING_LIGHT = WARNING_BG
    ERROR_LIGHT = ERROR_BG