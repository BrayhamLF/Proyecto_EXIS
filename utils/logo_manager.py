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
            AssetManager.logo("shield.png"),
            size
        )

    @staticmethod
    def horizontal(size):

        return ImageLoader.load(
            AssetManager.logo("horizontal.png"),
            size
        )

    @staticmethod
    def white(size):

        return ImageLoader.load(
            AssetManager.logo("white.png"),
            size
        )