"""
icon_manager.py
---------------
"""

from utils.asset_manager import AssetManager
from utils.image_loader import ImageLoader


class IconManager:

    @staticmethod
    def load(name: str, size=(22, 22)):

        filename = name if name.endswith(".svg") else f"{name}.svg"
        return ImageLoader.load(AssetManager.icon(filename), size)
