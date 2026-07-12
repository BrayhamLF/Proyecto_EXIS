"""
icon_manager.py
---------------
"""

from utils.asset_manager import AssetManager
from utils.image_loader import ImageLoader


class IconManager:

    @staticmethod
    def load(name: str, size=(22, 22)):

        return ImageLoader.load(
            AssetManager.icon(f"{name}.png"),
            size
        )