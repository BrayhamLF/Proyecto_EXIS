"""
header_actions.py
-----------------

Zona derecha del Header.

Contiene:

- Notificaciones
- Avatar
- Nombre
- Rol
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts

from utils.icons import Icons


class HeaderActions(ctk.CTkFrame):

    def __init__(
        self,
        master,
        notification_callback=None
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.notification_callback = notification_callback

        self.notification_icon = None

        self.user_name = None
        self.user_role = None

        self.avatar = None

        self._build()

    # ==================================================
    # Construcción
    # ==================================================

    def _build(self):

        # ------------------------------------------
        # Botón notificaciones
        # ------------------------------------------

        self.notification_icon = Icons.notification(
            (20,20)
        )

        self.notification_button = ctk.CTkButton(

            self,

            text="",

            image=self.notification_icon,

            width=40,

            height=40,

            fg_color="transparent",

            hover_color=Colors.SURFACE_ALT,

            command=self._notification_clicked

        )

        self.notification_button.pack(

            side="left",

            padx=(0,20)

        )

        # ------------------------------------------
        # Avatar
        # ------------------------------------------

        self.avatar = ctk.CTkLabel(

            self,

            text="A",

            width=38,

            height=38,

            corner_radius=19,

            fg_color=Colors.PRIMARY,

            text_color=Colors.TEXT_WHITE,

            font=Fonts.BODY_BOLD

        )

        self.avatar.pack(

            side="left",

            padx=(0,12)

        )

        # ------------------------------------------
        # Información
        # ------------------------------------------

        info = ctk.CTkFrame(

            self,

            fg_color="transparent"

        )

        info.pack(

            side="left"

        )

        self.user_name = ctk.CTkLabel(

            info,

            text="Administrador",

            font=Fonts.BODY_BOLD,

            text_color=Colors.TEXT

        )

        self.user_name.pack(

            anchor="w"

        )

        self.user_role = ctk.CTkLabel(

            info,

            text="Administrador",

            font=Fonts.SMALL,

            text_color=Colors.TEXT_SECONDARY

        )

        self.user_role.pack(

            anchor="w"

        )

    # ==================================================
    # Eventos
    # ==================================================

    def _notification_clicked(self):

        if self.notification_callback:

            self.notification_callback()

    # ==================================================
    # API
    # ==================================================

    def set_user(
        self,
        name,
        role
    ):

        self.user_name.configure(
            text=name
        )

        self.user_role.configure(
            text=role
        )

        self.avatar.configure(
            text=name[0].upper()
        )

    def set_notification_callback(
        self,
        callback
    ):

        self.notification_callback = callback