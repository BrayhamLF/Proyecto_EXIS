"""Botón de navegación para el sidebar institucional."""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors


class SidebarButton(ctk.CTkFrame):
    HEIGHT = 38

    def __init__(self, master, text: str, icon=None, command=None):
        super().__init__(master, height=self.HEIGHT, fg_color="transparent")

        self.command = command
        self.active = False
        self.collapsed = False
        self.text = text
        self.icon = icon

        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)

        self.button = ctk.CTkButton(
            self,
            text=text,
            image=icon,
            compound="left",
            anchor="w",
            height=self.HEIGHT,
            corner_radius=7,
            fg_color="transparent",
            hover_color=Colors.PRIMARY_HOVER,
            text_color=Colors.TEXT_WHITE,
            font=("Segoe UI", 13),
            border_width=0,
            command=self._clicked,
        )
        self.button.grid(row=0, column=0, sticky="ew")

    def _clicked(self) -> None:
        if self.command is not None:
            self.command()

    def set_active(self) -> None:
        self.active = True
        self.button.configure(
            fg_color=Colors.SECONDARY,
            hover_color=Colors.SECONDARY,
            text_color=Colors.TEXT_WHITE,
            font=("Segoe UI", 13, "bold"),
        )

    def set_inactive(self) -> None:
        self.active = False
        self.button.configure(
            fg_color="transparent",
            hover_color=Colors.PRIMARY_HOVER,
            text_color=Colors.TEXT_WHITE,
            font=("Segoe UI", 13),
        )

    def collapse(self) -> None:
        if self.collapsed:
            return

        self.collapsed = True
        self.button.configure(text="", width=44, anchor="center", compound="image")

    def expand(self) -> None:
        if not self.collapsed:
            return

        self.collapsed = False
        self.button.configure(text=self.text, width=0, anchor="w", compound="left")

    def set_text(self, text: str) -> None:
        self.text = text
        if not self.collapsed:
            self.button.configure(text=text)

    def set_icon(self, icon) -> None:
        self.icon = icon
        self.button.configure(image=icon)
