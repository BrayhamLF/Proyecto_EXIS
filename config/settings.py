"""
settings.py
-----------

Configuración global del Sistema de Gestión de
Monitorías y Tutorías Académicas.
"""

from pathlib import Path

# Tamaños reutilizables
from config.sizes import Sizes


class Settings:

    # ==================================================
    # PROYECTO
    # ==================================================

    BASE_DIR = Path(__file__).resolve().parent.parent

    # ==================================================
    # RECURSOS
    # ==================================================

    ASSETS_PATH = BASE_DIR / "assets"

    LOGOS_PATH = ASSETS_PATH / "logos"

    ICONS_PATH = ASSETS_PATH / "icons"

    IMAGES_PATH = ASSETS_PATH / "images"

    FONTS_PATH = ASSETS_PATH / "fonts"

    # ==================================================
    # IMÁGENES
    # ==================================================

    APP_LOGO = LOGOS_PATH / "escudo-unitropico_2.png"

    # Compatibilidad: ruta del logo singular
    LOGO_PATH = APP_LOGO

    DEFAULT_AVATAR = ICONS_PATH / "usuario.png"

    DEFAULT_USER_ICON = ICONS_PATH / "usuario.png"

    DEFAULT_PASSWORD_ICON = ICONS_PATH / "cerrar.png"

    # ==================================================
    # INFORMACIÓN DEL SISTEMA
    # ==================================================

    APP_NAME = "Monitorías y Tutorías Académicas"

    APP_SHORT_NAME = "Monitorías"

    VERSION = "1.0.0"

    COMPANY = "Universidad Internacional del Trópico Americano"

    # ==================================================
    # VENTANA
    # ==================================================

    WINDOW_WIDTH = 1366

    WINDOW_HEIGHT = 768

    MIN_WIDTH = 1180

    MIN_HEIGHT = 720

    # ==================================================
    # LOGIN
    # ==================================================

    LOGIN_LEFT_WIDTH = 420

    LOGIN_FORM_WIDTH = 540

    LOGIN_LOGO_HEIGHT = 240

    # ==================================================
    # ANIMACIONES
    # ==================================================

    FADE_TIME = 150

    # ==================================================
    # BASE DE DATOS
    # ==================================================

    DB_HOST = "localhost"

    DB_PORT = 3306

    DB_NAME = "monitorias"

    # ==================================================
    # DEBUG
    # ==================================================

    DEBUG = True
    
    # ==================================================
    # ICONOS
    # ==================================================

    DASHBOARD_ICON = ICONS_PATH / "inicio.png"

    STUDENTS_ICON = ICONS_PATH / "estudiante.png"

    USERS_ICON = ICONS_PATH / "usuario.png "

    TUTORS_ICON = ICONS_PATH / "tutor.png"

    MONITORS_ICON = ICONS_PATH / "monitor.png"

    TUTORIALS_ICON = ICONS_PATH / "tutoria.png"

    SESSIONS_ICON = ICONS_PATH / "sesiones.png"

    TRACKING_ICON = ICONS_PATH / "seguimiento.png"

    SPACES_ICON = ICONS_PATH / "espacio.png"

    REPORTS_ICON = ICONS_PATH / "reporte.png"

    SETTINGS_ICON = ICONS_PATH / "configuracion.png"

    LOGOUT_ICON = ICONS_PATH / "salida.png"

    MENU_ICON = ICONS_PATH / "menu_1.png"

    SEARCH_ICON = ICONS_PATH / "buscar.png"

    NOTIFICATION_ICON = ICONS_PATH / "notificacion.png"

    EYE_ICON = ICONS_PATH / "mostrar.png"

    EYE_OFF_ICON = ICONS_PATH / "ocultar.png"
    
    ARROW_RIGHT_ICON = ICONS_PATH / "flecha-derecha.png"
    
    # Tamaños de iconos (ancho, alto)
    ICON_SIZE = (Sizes.SIDEBAR_ICON, Sizes.SIDEBAR_ICON)

    STATISTIC_ICON_SIZE = (Sizes.ICON_XL, Sizes.ICON_XL)
