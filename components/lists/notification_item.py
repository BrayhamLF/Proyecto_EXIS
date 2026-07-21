"""
notification_item.py
--------------------

Elemento reutilizable para notificaciones.
"""

from __future__ import annotations

from components.lists.list_item import ListItem


class NotificationItem(ListItem):

    def __init__(
        self,
        master,
        title,
        description,
        icon=None,
        command=None
    ):

        super().__init__(
            master,
            icon=icon,
            title=title,
            subtitle=description,
            trailing="",
            command=command
        )