"""Barra superior compacta de la zona autenticada."""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from utils.icons import Icons


class Header(ctk.CTkFrame):
    """Contiene el control del sidebar y el acceso a notificaciones."""

    HEIGHT = 60

    def __init__(self, master, menu_callback=None, notification_callback=None):
        super().__init__(
            master,
            height=self.HEIGHT,
            fg_color=Colors.SURFACE,
            corner_radius=0,
        )

        self.menu_callback = menu_callback
        self.notification_callback = notification_callback
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)

        self._build()

    def _build(self) -> None:
        # Notification button (moved to the right). The sidebar toggle/menu button was removed per request.
        self.notification_icon = Icons.notification((18, 18))
        ctk.CTkButton(
            self,
            text="",
            image=self.notification_icon,
            width=42,
            height=42,
            fg_color="transparent",
            hover_color=Colors.SURFACE_ALT,
            corner_radius=8,
            command=self._notification_clicked,
        ).grid(row=0, column=1, padx=(10, 20), pady=9)

        ctk.CTkFrame(self, height=1, fg_color=Colors.BORDER, corner_radius=0).grid(
            row=1, column=0, columnspan=2, sticky="ew"
        )

    def _menu_clicked(self) -> None:
        if self.menu_callback is not None:
            self.menu_callback()

    def _notification_clicked(self) -> None:
        if self.notification_callback is not None:
            self.notification_callback()

    def set_title(self, title: str, subtitle: str = "") -> None:
        """Compatibilidad: el título ahora se muestra dentro de cada página."""

    def set_user(self, user: str, role: str) -> None:
        """Compatibilidad: el usuario se visualiza en el pie del sidebar."""

    def set_notification_callback(self, callback) -> None:
        self.notification_callback = callback
