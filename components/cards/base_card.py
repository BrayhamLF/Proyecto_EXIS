"""
base_card.py
------------

Tarjeta base reutilizable para todo el sistema.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.sizes import Sizes


class BaseCard(ctk.CTkFrame):

    def __init__(
        self,
        master,
        width: int | None = None,
        height: int | None = None,
        fg_color: str | None = None,
        corner_radius: int | None = None,
        border_width: int = 1,
        border_color: str | None = None,
        propagate: bool | None = None,
        **kwargs
    ):

        init_kwargs = {

            "fg_color": fg_color or Colors.SURFACE,

            "corner_radius": corner_radius or Sizes.LARGE_RADIUS,

            "border_width": border_width,

            "border_color": border_color or Colors.BORDER,

        }

        if width is not None:
            init_kwargs["width"] = width

        if height is not None:
            init_kwargs["height"] = height

        init_kwargs.update(kwargs)

        super().__init__(master, **init_kwargs)

        # ==================================================
        # Grid principal
        # ==================================================

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ==================================================
        # Contenedor interno
        # ==================================================

        self.content = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.content.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        # ==================================================
        # Propagación inteligente
        # ==================================================

        if propagate is None:

            propagate = (

                width is None

                and

                height is None

            )

        self.grid_propagate(propagate)
        self.pack_propagate(propagate)

    # ==================================================
    # API
    # ==================================================

    def enable_propagation(self):

        self.grid_propagate(True)
        self.pack_propagate(True)

    def disable_propagation(self):

        self.grid_propagate(False)
        self.pack_propagate(False)

    def set_fixed_size(
        self,
        width=None,
        height=None
    ):

        if width is not None:
            self.configure(width=width)

        if height is not None:
            self.configure(height=height)

        self.disable_propagation()

    def clear(self):

        for widget in self.content.winfo_children():
            widget.destroy()