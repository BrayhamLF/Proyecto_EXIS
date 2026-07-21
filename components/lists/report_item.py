"""
report_item.py
--------------

Elemento reutilizable para reportes.
"""

from __future__ import annotations

from components.lists.list_item import ListItem


class ReportItem(ListItem):

    def __init__(
        self,
        master,
        report,
        generated,
        status="Generado",
        icon=None,
        command=None
    ):

        super().__init__(
            master,
            icon=icon,
            title=report,
            subtitle=generated,
            trailing=status,
            command=command
        )