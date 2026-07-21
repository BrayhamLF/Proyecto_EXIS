"""
list_item.py
------------

Componente base para elementos de listas del sistema.
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts
from config.sizes import Sizes


class ListItem(ctk.CTkFrame):

    HEIGHT = 68

    def __init__(
        self,
        master,
        title="",
        subtitle="",
        command=None
    ):

        super().__init__(

            master,

            height=self.HEIGHT,

            fg_color="transparent",

            corner_radius=Sizes.MEDIUM_RADIUS

        )

        self.command = command

        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self._build()

        self.set_title(title)

        self.set_subtitle(subtitle)

        # Attach event bindings (use a distinct method name to avoid
        # shadowing tkinter's internal _bind implementation.)
        self._bind_events()

    # =====================================================
    # Construcción
    # =====================================================

    def _build(self):

        # -----------------------------------------
        # Leading
        # -----------------------------------------

        self.leading_frame = ctk.CTkFrame(

            self,

            fg_color="transparent",

            width=48

        )

        self.leading_frame.grid(

            row=0,

            column=0,

            sticky="ns",

            padx=(0,12)

        )

        # -----------------------------------------
        # Content
        # -----------------------------------------

        self.content_frame = ctk.CTkFrame(

            self,

            fg_color="transparent"

        )

        self.content_frame.grid(

            row=0,

            column=1,

            sticky="nsew"

        )

        self.content_frame.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(

            self.content_frame,

            text="",

            anchor="w",

            font=Fonts.BODY_BOLD,

            text_color=Colors.TEXT

        )

        self.title_label.pack(

            anchor="w"

        )

        self.subtitle_label = ctk.CTkLabel(

            self.content_frame,

            text="",

            anchor="w",

            font=Fonts.SMALL,

            text_color=Colors.TEXT_SECONDARY

        )

        self.subtitle_label.pack(

            anchor="w",

            pady=(2,0)

        )

        # -----------------------------------------
        # Trailing
        # -----------------------------------------

        self.trailing_frame = ctk.CTkFrame(

            self,

            fg_color="transparent"

        )

        self.trailing_frame.grid(

            row=0,

            column=2,

            sticky="e",

            padx=(15,0)

        )

    # =====================================================
    # Eventos
    # =====================================================

    def _bind_events(self):

        widgets = [

            self,

            self.leading_frame,

            self.content_frame,

            self.trailing_frame,

            self.title_label,

            self.subtitle_label

        ]

        for widget in widgets:

            widget.bind("<Button-1>", self._clicked)

            widget.bind("<Enter>", self._hover_enter)

            widget.bind("<Leave>", self._hover_leave)

    def _clicked(self, event=None):

        if callable(self.command):

            self.command()

    def _hover_enter(self, event=None):

        self.configure(

            fg_color=Colors.SURFACE_ALT

        )

    def _hover_leave(self, event=None):

        self.configure(

            fg_color="transparent"

        )

    # =====================================================
    # API
    # =====================================================

    def set_title(self, text):

        self.title_label.configure(text=text)

    def set_subtitle(self, text):

        self.subtitle_label.configure(text=text)