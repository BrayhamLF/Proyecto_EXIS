"""
icons.py
--------

Administrador centralizado de iconos del sistema.
"""

from __future__ import annotations

from utils.image_loader import ImageLoader
from config.settings import Settings


class Icons:

    DEFAULT_SIZE = (22, 22)

    _cache = {}

    # ==================================================
    # Método privado
    # ==================================================

    @classmethod
    def _load(cls, path, size=None):

        if size is None:
            size = cls.DEFAULT_SIZE

        key = (str(path), tuple(size))

        if key not in cls._cache:
            cls._cache[key] = ImageLoader.load(path, size)

        return cls._cache[key]

    # ==================================================
    # API Genérica
    # ==================================================

    @classmethod
    def load(cls, path, size=None):
        """
        Permite cargar cualquier icono sin crear un método
        específico para él.
        """
        return cls._load(path, size)

    @classmethod
    def clear_cache(cls):
        """
        Limpia la caché de iconos.
        Útil durante el desarrollo.
        """
        cls._cache.clear()

    # ==================================================
    # Navegación
    # ==================================================

    @classmethod
    def dashboard(cls, size=None):
        return cls._load(Settings.DASHBOARD_ICON, size)

    @classmethod
    def students(cls, size=None):
        return cls._load(Settings.STUDENTS_ICON, size)

    @classmethod
    def users(cls, size=None):
        return cls._load(Settings.USERS_ICON, size)

    @classmethod
    def tutors(cls, size=None):
        return cls._load(Settings.TUTORS_ICON, size)

    @classmethod
    def monitors(cls, size=None):
        return cls._load(Settings.MONITORS_ICON, size)

    @classmethod
    def tutorials(cls, size=None):
        return cls._load(Settings.TUTORIALS_ICON, size)

    @classmethod
    def sessions(cls, size=None):
        return cls._load(Settings.SESSIONS_ICON, size)

    @classmethod
    def tracking(cls, size=None):
        return cls._load(Settings.TRACKING_ICON, size)

    @classmethod
    def spaces(cls, size=None):
        return cls._load(Settings.SPACES_ICON, size)

    @classmethod
    def reports(cls, size=None):
        return cls._load(Settings.REPORTS_ICON, size)

    @classmethod
    def settings(cls, size=None):
        return cls._load(Settings.SETTINGS_ICON, size)

    @classmethod
    def logout(cls, size=None):
        return cls._load(Settings.LOGOUT_ICON, size)

    # ==================================================
    # Header
    # ==================================================

    @classmethod
    def menu(cls, size=None):
        return cls._load(Settings.MENU_ICON, size)

    @classmethod
    def search(cls, size=None):
        return cls._load(Settings.SEARCH_ICON, size)

    @classmethod
    def notification(cls, size=None):
        return cls._load(Settings.NOTIFICATION_ICON, size)

    @classmethod
    def user(cls, size=None):
        return cls._load(Settings.USER_ICON, size)

    # ==================================================
    # Formularios
    # ==================================================

    @classmethod
    def eye(cls, size=None):
        return cls._load(Settings.EYE_ICON, size)

    @classmethod
    def eye_off(cls, size=None):
        return cls._load(Settings.EYE_OFF_ICON, size)

    # ==========================================
    # Obtención dinámica
    # ==========================================

    @classmethod
    def get(cls, name: str, size=None):

        method = getattr(cls, name, None)

        if callable(method):
            return method(size)

        return None

    # ==========================================
    # Dashboard
    # ==========================================

    @classmethod
    def arrow_right(cls, size=None):
        return cls._load(Settings.ARROW_RIGHT_ICON, size)