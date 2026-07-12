"""
sidebar.py
----------

Barra lateral principal de la aplicación.
"""

from __future__ import annotations

import customtkinter as ctk

from components.navigation.sidebar_button import SidebarButton

from config.colors import Colors
from config.fonts import Fonts
from config.navigation import MAIN_MENU
from config.settings import Settings

from utils.image_loader import ImageLoader


class Sidebar(ctk.CTkFrame):

    def __init__(
        self,
        master,
        width=260,
        command=None
    ):

        super().__init__(
            master,
            width=width,
            fg_color=Colors.SIDEBAR,
            corner_radius=0
        )

        self.command = command

        self.buttons = {}

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._build()

    # =====================================================
    # CONSTRUCCIÓN
    # =====================================================

    def _build(self):

        self._build_header()

        self._build_menu()

        self._build_footer()

    # =====================================================
    # HEADER
    # =====================================================

    def _build_header(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(25, 20),
            padx=15
        )

        logo = ImageLoader.load(
            Settings.LOGO_PATH,
            (90, 90)
        )

        lbl_logo = ctk.CTkLabel(
            frame,
            image=logo,
            text=""
        )

        lbl_logo.pack(pady=(0, 12))

        lbl_title = ctk.CTkLabel(
            frame,
            text="Monitorías y\nTutorías Académicas",
            font=Fonts.H3,
            justify="center",
            text_color=Colors.WHITE
        )

        lbl_title.pack()

    # =====================================================
    # MENÚ
    # =====================================================

    def _build_menu(self):

        frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10
        )

        for item in MAIN_MENU:

            icon = ImageLoader.load(
                f"{Settings.ICONS_PATH}{item.icon}",
                Settings.ICON_SIZE
            )

            button = SidebarButton(
                frame,
                text=item.title,
                icon=icon,
                command=lambda i=item: self._on_selected(i.id)
            )

            button.pack(
                fill="x",
                pady=4
            )

            self.buttons[item.id] = button

    # =====================================================
    # FOOTER
    # =====================================================

    def _build_footer(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=15,
            pady=15
        )

        self.user_label = ctk.CTkLabel(
            frame,
            text="Invitado",
            font=Fonts.BODY_BOLD,
            text_color=Colors.WHITE
        )

        self.user_label.pack(
            anchor="w"
        )

        self.role_label = ctk.CTkLabel(
            frame,
            text="Sin iniciar sesión",
            font=Fonts.SMALL,
            text_color=Colors.LIGHT
        )

        self.role_label.pack(
            anchor="w",
            pady=(0, 12)
        )

        logout = ctk.CTkButton(
            frame,
            text="Cerrar sesión",
            fg_color="transparent",
            hover_color=Colors.SIDEBAR_HOVER,
            anchor="w",
            command=self._logout
        )

        logout.pack(
            fill="x"
        )

    # =====================================================
    # EVENTOS
    # =====================================================

    def _on_selected(
        self,
        option: str
    ):

        for button in self.buttons.values():
            button.set_inactive()

        self.buttons[option].set_active()

        if self.command:
            self.command(option)

    def _logout(self):

        if self.command:
            self.command("logout")

    # =====================================================
    # API
    # =====================================================

    def set_user(
        self,
        name: str,
        role: str
    ):

        self.user_label.configure(
            text=name
        )

        self.role_label.configure(
            text=role
        )