"""
image_loader.py
---------------

Utilidad para cargar imágenes del sistema.
"""

from __future__ import annotations

from pathlib import Path

import customtkinter as ctk

from PIL import Image


class ImageLoader:

    _cache: dict = {}

    @classmethod
    def load(
        cls,
        path: str | Path,
        size: tuple[int | None, int | None]
    ) -> ctk.CTkImage | None:

        image_path = Path(path)

        cache_key = (str(image_path.resolve()), size)

        if cache_key in cls._cache:
            return cls._cache[cache_key]

        if not image_path.exists():

            print(f"[ImageLoader] No existe el archivo:\n{image_path}")

            return None

        if image_path.is_dir():

            print(f"[ImageLoader] Se esperaba una imagen y se recibió una carpeta:\n{image_path}")

            return None

        try:

            image = Image.open(image_path)

            original_width, original_height = image.size
            requested_width, requested_height = size

            if requested_width is None and requested_height is None:
                final_size = image.size
            elif requested_width is None:
                ratio = requested_height / original_height
                final_size = (max(1, int(original_width * ratio)), requested_height)
            elif requested_height is None:
                ratio = requested_width / original_width
                final_size = (requested_width, max(1, int(original_height * ratio)))
            else:
                ratio = min(
                    requested_width / original_width,
                    requested_height / original_height
                )
                final_size = (
                    max(1, int(original_width * ratio)),
                    max(1, int(original_height * ratio))
                )

            ctk_image = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=final_size
            )

            cls._cache[cache_key] = ctk_image

            return ctk_image

        except Exception as error:

            print(
                "[ImageLoader] Error cargando imagen:\n"
                f"{image_path}\n"
                f"{error}"
            )

            return None

    # ==================================================
    # API
    # ==================================================

    @classmethod
    def clear_cache(cls):

        cls._cache.clear()