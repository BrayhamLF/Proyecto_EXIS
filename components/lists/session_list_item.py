"""
session_list_item.py
--------------------

Elemento compacto para representar una monitoría
dentro del Dashboard.
"""

from __future__ import annotations

import customtkinter as ctk

from components.lists.list_item import ListItem
from components.ui.icon_circle import IconCircle
from components.ui.status_badge import StatusBadge

from config.colors import Colors

from utils.icons import Icons


class SessionListItem(ListItem):

    STATUS_COLORS = {

        "Disponible": (
            Colors.SUCCESS_BG,
            Colors.SUCCESS
        ),

        "Próxima": (
            Colors.PRIMARY_LIGHT,
            Colors.PRIMARY
        ),

        "En curso": (
            Colors.WARNING_BG,
            Colors.WARNING
        )

    }

    def __init__(

        self,

        master,

        subject,

        monitor,

        date,

        hour,

        status="Disponible",

        command=None

    ):

        self.subject = subject
        self.monitor = monitor
        self.date = date
        self.hour = hour
        self.current_status = status

        super().__init__(

            master,

            title=subject,

            subtitle=f"{monitor} • {date} • {hour}",

            command=command

        )

        self._build_icon()

        self._build_status()

    # ==================================================

    def _build_icon(self):

        self.icon = IconCircle(

            self.leading_frame,

            image=Icons.sessions((18,18)),

            size=40,

            color=Colors.PRIMARY

        )

        self.icon.pack(expand=True)

    # ==================================================

    def _build_status(self):

        fg,text = self.STATUS_COLORS.get(

            self.current_status,

            (
                Colors.SUCCESS_BG,
                Colors.SUCCESS
            )

        )

        self.badge = StatusBadge(

            self.trailing_frame,

            text=self.current_status,

            fg_color=fg,

            text_color=text

        )

        self.badge.pack()

    # ==================================================

    def set_status(self,status):

        self.current_status = status

        fg,text = self.STATUS_COLORS.get(

            status,

            (
                Colors.SUCCESS_BG,
                Colors.SUCCESS
            )

        )

        self.badge.configure(

            text=status,

            fg_color=fg,

            text_color=text

        )