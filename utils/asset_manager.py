"""
asset_manager.py
----------------

Administrador centralizado de recursos.
"""

from config.settings import Settings


class AssetManager:

    ROOT = Settings.ASSETS_PATH

    ICONS = ROOT / "icons"

    LOGOS = ROOT / "logos"

    IMAGES = ROOT / "images"

    @classmethod
    def icon(cls, filename: str):

        return cls.ICONS / filename

    @classmethod
    def logo(cls, filename: str):

        return cls.LOGOS / filename

    @classmethod
    def image(cls, filename: str):

        return cls.IMAGES / filename
