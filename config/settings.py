"""
settings.py
-----------

Configuración global del Sistema de Gestión de
Monitorías y Tutorías Académicas.
"""

from pathlib import Path


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

    IMAGES_PATH = ASSETS_PATH / "images"

    ICONS_PATH = ASSETS_PATH / "icons"

    FONTS_PATH = ASSETS_PATH / "fonts"

    # ==================================================
    # IMÁGENES
    # ==================================================

    APP_LOGO = LOGOS_PATH / "escudo-unitropico_1.png"

    LOGIN_BANNER = IMAGES_PATH / "login_banner.png"

    DEFAULT_AVATAR = IMAGES_PATH / "avatar.png"

    DEFAULT_USER_ICON = ICONS_PATH / "user.png"

    DEFAULT_PASSWORD_ICON = ICONS_PATH / "password.png"

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