"""
statistic_grid.py
-----------------

Contenedor de tarjetas estadísticas del Dashboard.
"""

from __future__ import annotations

import customtkinter as ctk

from config.sizes import Sizes


class StatisticGrid(ctk.CTkFrame):

    def __init__(
        self,
        master,
        columns: int = 4,
        spacing: int = Sizes.SPACE_16
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.columns = columns
        self.spacing = spacing
        self.cards = []

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    # ==================================================
    # API Pública
    # ==================================================

    def add_card(self, card):

        index = len(self.cards)

        row = index // self.columns
        column = index % self.columns

        self.grid_rowconfigure(row, weight=1)

        card.grid(
            row=row,
            column=column,
            padx=self.spacing // 2,
            pady=self.spacing // 2,
            sticky="nsew"
        )

        self.cards.append(card)

    def clear(self):
        """
        Elimina todas las tarjetas del grid.
        """

        for card in self.cards:
            card.destroy()

        self.cards.clear()

    def get_cards(self):
        """
        Retorna la lista de tarjetas actuales.
        """

        return self.cards