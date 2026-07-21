"""Tarjeta compacta de indicador para el dashboard administrativo."""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors


class AdminMetricCard(ctk.CTkFrame):
    """Muestra un indicador principal siguiendo la grilla del dashboard."""

    def __init__(
        self,
        master,
        title: str,
        value: int | str = 0,
        icon=None,
        background: str = Colors.SURFACE_ALT,
    ):
        super().__init__(
            master,
            height=126,
            fg_color=background,
            corner_radius=10,
            border_width=0,
        )

        self.grid_propagate(False)
        self.grid_columnconfigure(1, weight=1)

        self._build(title, value, icon)

    def _build(self, title: str, value: int | str, icon) -> None:
        if icon is not None:
            ctk.CTkLabel(self, text="", image=icon).grid(
                row=0, column=0, padx=(22, 10), pady=(23, 0), sticky="w"
            )

        ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 13, "bold"),
            text_color=Colors.TEXT,
            anchor="w",
        ).grid(row=0, column=1, padx=(0, 10), pady=(23, 0), sticky="w")

        ctk.CTkLabel(
            self,
            text="›",
            font=("Segoe UI", 23),
            text_color=Colors.PRIMARY,
        ).grid(row=0, column=2, padx=(0, 22), pady=(20, 0), sticky="e")

        self.value_label = ctk.CTkLabel(
            self,
            text=str(value),
            font=("Segoe UI", 31, "bold"),
            text_color=Colors.BLACK,
            anchor="w",
        )
        self.value_label.grid(
            row=1, column=0, columnspan=3, padx=26, pady=(3, 21), sticky="w"
        )

    def set_value(self, value: int | str) -> None:
        self.value_label.configure(text=str(value))
