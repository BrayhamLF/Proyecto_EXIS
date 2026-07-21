"""
activity_item.py
----------------

Elemento visual para representar una actividad reciente.
"""

from __future__ import annotations

from components.lists.list_item import ListItem
from components.ui.icon_circle import IconCircle

from config.colors import Colors


class ActivityItem(ListItem):

    def __init__(
        self,
        master,
        title,
        description,
        time,
        icon,
        color=Colors.SUCCESS,
        command=None
    ):

        self.description = description
        self.time = time

        super().__init__(

            master,

            title=title,

            subtitle=f"{description} • {time}",

            command=command

        )

        self.avatar = IconCircle(

            self.leading_frame,

            image=icon,

            size=40,

            color=color

        )

        self.avatar.pack(expand=True)