"""
dashboard_table.py
------------------

Tabla institucional reutilizable para el Dashboard.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class DashboardTable(ctk.CTkFrame):

    def __init__(
        self,
        master,
        columns: list[str]
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.columns = columns

        self.rows = []

        self._build()

    # ==================================================

    def _build(self):

        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=1)

        self._build_header()

        self._build_body()

    # ==================================================

    def _build_header(self):

        self.header = ctk.CTkFrame(

            self,

            fg_color=Colors.SURFACE_ALT,

            corner_radius=10,

            height=42

        )

        self.header.grid(

            row=0,

            column=0,

            sticky="ew"

        )

        total = len(self.columns)

        for column in range(total):

            self.header.grid_columnconfigure(
                column,
                weight=1
            )

        for column, title in enumerate(self.columns):

            label = ctk.CTkLabel(

                self.header,

                text=title,

                font=Fonts.SMALL_BOLD,

                text_color=Colors.TEXT

            )

            label.grid(

                row=0,

                column=column,

                padx=15,

                pady=12,

                sticky="w"

            )

    # ==================================================

    def _build_body(self):

        self.body = ctk.CTkScrollableFrame(

            self,

            fg_color="transparent"

        )

        self.body.grid(

            row=1,

            column=0,

            sticky="nsew",

            pady=(10,0)

        )

        self.body.grid_columnconfigure(
            0,
            weight=1
        )

        self.empty_label = ctk.CTkLabel(

            self.body,

            text="No existen registros disponibles.",

            font=Fonts.BODY,

            text_color=Colors.TEXT_SECONDARY

        )

        self.empty_label.grid(

            row=0,

            column=0,

            pady=40

        )

    # ==================================================
    # API
    # ==================================================

    def clear(self):

        for widget in self.body.winfo_children():

            widget.destroy()

        self.rows.clear()

    def set_rows(self, rows):

        self.clear()

        if not rows:

            self.empty_label = ctk.CTkLabel(

                self.body,

                text="No existen registros disponibles.",

                font=Fonts.BODY,

                text_color=Colors.TEXT_SECONDARY

            )

            self.empty_label.grid(
                row=0,
                column=0,
                pady=40
            )

            return

        for row_index, row in enumerate(rows):

            frame = ctk.CTkFrame(

                self.body,

                fg_color="transparent"

            )

            frame.grid(

                row=row_index,

                column=0,

                sticky="ew",

                pady=4

            )

            for column in range(len(self.columns)):

                frame.grid_columnconfigure(
                    column,
                    weight=1
                )

            for column, value in enumerate(row):

                ctk.CTkLabel(

                    frame,

                    text=str(value),

                    font=Fonts.BODY,

                    text_color=Colors.TEXT

                ).grid(

                    row=0,

                    column=column,

                    sticky="w",

                    padx=15,

                    pady=8

                )

            self.rows.append(frame)