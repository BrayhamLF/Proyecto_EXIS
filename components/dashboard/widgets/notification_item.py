"""
notification_item.py
--------------------
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class NotificationItem(ctk.CTkFrame):

    def __init__(
        self,
        master,
        text=""
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.grid_columnconfigure(1, weight=1)

        icon = ctk.CTkLabel(
            self,
            text="🔔",
            font=Fonts.BODY
        )

        icon.grid(
            row=0,
            column=0,
            padx=(0,12)
        )

        label = ctk.CTkLabel(
            self,
            text=text,
            anchor="w",
            justify="left",
            font=Fonts.BODY,
            text_color=Colors.TEXT
        )

        label.grid(
            row=0,
            column=1,
            sticky="ew"
        )