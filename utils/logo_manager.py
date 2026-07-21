"""
logo_manager.py
---------------
"""

from utils.asset_manager import AssetManager
from utils.image_loader import ImageLoader


class LogoManager:

    @staticmethod
    def shield(size):

        return ImageLoader.load(
            AssetManager.logo("escudo-unitropico_2.png"),
            size
        )

    @staticmethod
    def horizontal(size):

        return ImageLoader.load(
            AssetManager.logo("logo-unitropico-02.png"),
            size
        )

    @staticmethod
    def white(size):

        return ImageLoader.load(
            AssetManager.logo("logo-simbolo-unitropico-2.png"),
            size
        )
