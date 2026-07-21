"""
image_loader.py
---------------

Carga centralizada de imágenes e iconos.
"""

from __future__ import annotations

from io import BytesIO
from pathlib import Path

try:
    import cairosvg
    _CAIROSVG_AVAILABLE = True
except Exception:
    cairosvg = None
    _CAIROSVG_AVAILABLE = False

import customtkinter as ctk

from PIL import Image


class ImageLoader:

    _cache = {}

    # ==================================================
    # Imagen normal
    # ==================================================

    @classmethod
    def load(cls, path, size):

        key = (str(path), size)

        if key in cls._cache:
            return cls._cache[key]

        image_path = Path(path)

        def _make_placeholder(requested_size):
            # requested_size: tuple (w,h) where w or h can be None
            rw, rh = requested_size
            default = 24
            if rw is None and rh is None:
                rw = rh = default
            elif rw is None:
                rw = rh or default
            elif rh is None:
                rh = rw or default
            try:
                rw_i = int(rw)
                rh_i = int(rh)
            except Exception:
                rw_i = rh_i = default
            return Image.new("RGBA", (max(1, rw_i), max(1, rh_i)), (0, 0, 0, 0))

        if not image_path.exists():

            # Return a transparent placeholder image instead of printing errors
            image = _make_placeholder(size)

        else:

            if image_path.suffix.lower() == ".svg":

                image = cls._load_svg(image_path)

                if image is None:
                    # failed to load/convert SVG — use placeholder
                    image = _make_placeholder(size)

            else:

                try:
                    image = Image.open(image_path)
                    # Convert raster images to RGBA so transparency is preserved
                    if getattr(image, "mode", None) != "RGBA":
                        image = image.convert("RGBA")
                except Exception:
                    image = _make_placeholder(size)

        # Calcular tamaño final respetando la proporción si se pasa None
        try:
            original_width, original_height = image.size
        except Exception:
            # si image no es un PIL.Image, intentar obtener size directo
            original_width, original_height = (None, None)

        requested_width, requested_height = size

        if requested_width is None and requested_height is None:
            final_size = (original_width, original_height)
        elif requested_width is None:
            if original_height and original_height != 0:
                ratio = requested_height / original_height
                final_size = (max(1, int(original_width * ratio)), requested_height)
            else:
                final_size = (requested_height, requested_height)
        elif requested_height is None:
            if original_width and original_width != 0:
                ratio = requested_width / original_width
                final_size = (requested_width, max(1, int(original_height * ratio)))
            else:
                final_size = (requested_width, requested_width)
        else:
            # ajustar para que quepa en la caja solicitada sin deformar
            if original_width and original_height:
                ratio = min(requested_width / original_width, requested_height / original_height)
                final_size = (max(1, int(original_width * ratio)), max(1, int(original_height * ratio)))
            else:
                final_size = (requested_width, requested_height)

        image = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=final_size
        )

        cls._cache[key] = image

        return image

    # ==================================================
    # SVG
    # ==================================================

    @staticmethod
    def _load_svg(path):
        """Try loading an SVG file and returning a PIL.Image in RGBA.

        Uses multiple cairosvg entry points to handle environments where
        passing a file URL may fail (e.g., OneDrive paths with special
        characters). Falls back gracefully to None on any failure.
        """

        if not _CAIROSVG_AVAILABLE:
            # cairosvg (and/or its native cairo dependency) is not available
            # — skip attempts to convert the SVG and use a drawn fallback below.
            pass

        try:
            # First try: render by passing the file path as a URL
            png = cairosvg.svg2png(url=str(path), background_color=None)
            img = Image.open(BytesIO(png))
            if getattr(img, "mode", None) != "RGBA":
                img = img.convert("RGBA")
            return img
        except Exception:
            pass

        try:
            # Fallback: read the SVG bytes and render from bytestring
            with open(path, "rb") as f:
                svg_bytes = f.read()
            png = cairosvg.svg2png(bytestring=svg_bytes, background_color=None)
            img = Image.open(BytesIO(png))
            if getattr(img, "mode", None) != "RGBA":
                img = img.convert("RGBA")
            return img
        except Exception:
            # As a last resort (for environments without native cairo),
            # return a simple generated placeholder image with a visible
            # bell-like shape so the UI doesn't show a fully transparent icon.
            try:
                size = (64, 64)
                img = Image.new("RGBA", size, (0, 0, 0, 0))
                from PIL import ImageDraw
                draw = ImageDraw.Draw(img)
                w, h = size
                # Bell body (ellipse)
                draw.ellipse([(w*0.2, h*0.15), (w*0.8, h*0.6)], outline=(255,255,255,255), width=2)
                # Bell bottom arc
                draw.arc([(w*0.2, h*0.35), (w*0.8, h*0.85)], start=0, end=180, fill=(255,255,255,255), width=2)
                # Clapper
                draw.ellipse([(w*0.45, h*0.6), (w*0.55, h*0.7)], fill=(255,255,255,255))
                return img
            except Exception:
                return None