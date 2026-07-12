"""
stack_layout.py
---------------

Layout vertical.
"""

from __future__ import annotations

from components.core.base_component import BaseComponent


class StackLayout(BaseComponent):

    def configure_grid(self):

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.current_row = 0

    def add(

        self,

        widget,

        pady=10,

        sticky="ew"

    ):

        widget.grid(

            row=self.current_row,

            column=0,

            sticky=sticky,

            pady=pady

        )

        self.current_row += 1