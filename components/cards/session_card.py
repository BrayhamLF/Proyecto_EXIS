"""
session_card.py
---------------

Tarjeta utilizada para mostrar la próxima
monitoría o tutoría del Dashboard.
"""

from __future__ import annotations

import customtkinter as ctk

from components.cards.base_card import BaseCard
from components.ui.icon_circle import IconCircle

from config.colors import Colors
from config.fonts import Fonts

from utils.icons import Icons


class SessionCard(BaseCard):

    def __init__(
        self,
        master,
        subject: str,
        tutor: str,
        monitor: str,
        date: str,
        hour: str,
        location: str
    ):

        super().__init__(
            master,
            height=250
        )

        self.subject = subject
        self.tutor = tutor
        self.monitor = monitor
        self.date = date
        self.hour = hour
        self.location = location

        self._build()

    # =====================================================
    # Construcción
    # =====================================================

    def _build(self):

        self.content.grid_columnconfigure(1, weight=1)

        # --------------------------------------------
        # Icono
        # --------------------------------------------

        icon = IconCircle(

            self.content,

            image=Icons.sessions((22,22)),

            color=Colors.PRIMARY,

            size=52

        )

        icon.grid(

            row=0,

            column=0,

            rowspan=2,

            padx=(20,18),

            pady=(20,15)

        )

        # --------------------------------------------
        # Asignatura
        # --------------------------------------------

        title = ctk.CTkLabel(

            self.content,

            text=self.subject,

            font=Fonts.H3,

            text_color=Colors.TEXT

        )

        title.grid(

            row=0,

            column=1,

            sticky="w",

            pady=(20,2)

        )

        subtitle = ctk.CTkLabel(

            self.content,

            text="Próxima monitoría",

            font=Fonts.SMALL,

            text_color=Colors.TEXT_SECONDARY

        )

        subtitle.grid(

            row=1,

            column=1,

            sticky="w"

        )

        # --------------------------------------------
        # Información
        # --------------------------------------------

        body = ctk.CTkFrame(

            self.content,

            fg_color="transparent"

        )

        body.grid(

            row=2,

            column=0,

            columnspan=2,

            sticky="ew",

            padx=20,

            pady=(10,20)

        )

        body.grid_columnconfigure(1, weight=1)

        self._info(body,0,"Tutor",self.tutor)

        self._info(body,1,"Monitor",self.monitor)

        self._info(body,2,"Fecha",self.date)

        self._info(body,3,"Hora",self.hour)

        self._info(body,4,"Lugar",self.location)

    # =====================================================

    def _info(
        self,
        master,
        row,
        label,
        value
    ):

        lbl = ctk.CTkLabel(

            master,

            text=f"{label}:",

            font=Fonts.SMALL_BOLD,

            text_color=Colors.TEXT_SECONDARY

        )

        lbl.grid(

            row=row,

            column=0,

            sticky="w",

            pady=4

        )

        value_lbl = ctk.CTkLabel(

            master,

            text=value,

            font=Fonts.BODY,

            text_color=Colors.TEXT

        )

        value_lbl.grid(

            row=row,

            column=1,

            sticky="w",

            padx=(12,0),

            pady=4

        )

    # =====================================================
    # API
    # =====================================================

    def update_session(self, session: dict):

        """
        Preparado para la integración con MariaDB.

        Posteriormente actualizará los datos
        sin reconstruir la tarjeta.
        """

        pass