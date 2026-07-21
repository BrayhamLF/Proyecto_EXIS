"""
session_item.py
---------------

Elemento reutilizable para representar
una monitoría o tutoría.
"""

from __future__ import annotations

from components.lists.list_item import ListItem

from components.ui.icon_circle import IconCircle
from components.ui.status_badge import StatusBadge

from config.colors import Colors

from utils.icons import Icons


class SessionItem(ListItem):

    STATUS_COLORS = {

        "Disponible": (
            Colors.SUCCESS_BG,
            Colors.SUCCESS
        ),

        "Ocupado": (
            Colors.ERROR_BG,
            Colors.ERROR
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
        schedule,
        status="Disponible",
        icon=None,
        command=None
    ):

        self.current_status = status

        super().__init__(

            master,

            title=subject,

            subtitle=schedule,

            command=command

        )

        self.icon = IconCircle(

            self.leading_frame,

            image=icon or Icons.sessions((18,18)),

            size=40,

            color=Colors.PRIMARY

        )

        self.icon.pack(
            expand=True
        )

        fg, text = self.STATUS_COLORS.get(

            status,

            (
                Colors.SUCCESS_LIGHT,
                Colors.SUCCESS
            )

        )

        self.badge = StatusBadge(

            self.trailing_frame,

            text=status,

            fg_color=fg,

            text_color=text

        )

        self.badge.pack()

    # ==================================================

    def set_status(self, status):

        self.current_status = status

        fg, text = self.STATUS_COLORS.get(

            status,

            (
                Colors.SUCCESS_LIGHT,
                Colors.SUCCESS
            )

        )

        self.badge.configure(

            text=status,

            fg_color=fg,

            text_color=text

        )