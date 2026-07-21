"""Sidebar institucional, compacto y colapsable."""

from __future__ import annotations

import customtkinter as ctk

from components.layout.sidebar_menu import SidebarMenu
from components.layout.sidebar_profile import SidebarProfile
from components.buttons.logout_button import LogoutButton
from config.colors import Colors
from config.settings import Settings
from config.sizes import Sizes
from utils.image_loader import ImageLoader


class Sidebar(ctk.CTkFrame):
    EXPANDED_WIDTH = Sizes.SIDEBAR_WIDTH
    COLLAPSED_WIDTH = Sizes.SIDEBAR_COLLAPSED_WIDTH

    def __init__(self, master, width=EXPANDED_WIDTH, command=None):
        super().__init__(
            master,
            width=width,
            fg_color=Colors.PRIMARY,
            corner_radius=0,
        )

        self.command = command
        self.expanded = True
        self.current_role = "Administrador"
        self.logo = None

        self.grid_propagate(False)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._build()

    def _build(self) -> None:
        self._build_brand()
        self._build_menu()
        self._build_footer()

    def _build_brand(self) -> None:
        self.brand = ctk.CTkFrame(self, height=97, fg_color="transparent")
        self.brand.grid(row=0, column=0, sticky="ew")
        self.brand.grid_propagate(False)
        self.brand.grid_columnconfigure(1, weight=1)

        logo_badge = ctk.CTkFrame(
            self.brand,
            width=44,
            height=44,
            fg_color=Colors.TRANSPARENT,
            corner_radius=0,
        )
        logo_badge.grid(row=0, column=0, rowspan=2, padx=(20, 11), pady=(18, 16))
        logo_badge.grid_propagate(False)

        self.logo = ImageLoader.load(Settings.APP_LOGO, (27, 31))
        ctk.CTkLabel(logo_badge, text="", image=self.logo).place(
            relx=0.5, rely=0.5, anchor="center"
        )

        self.brand_name = ctk.CTkLabel(
            self.brand,
            text="UNITRÓPICO",
            font=("Segoe UI", 9, "bold"),
            text_color=Colors.SECONDARY,
            anchor="w",
        )
        self.brand_name.grid(row=0, column=1, sticky="sw", pady=(21, 0))

        self.system_name = ctk.CTkLabel(
            self.brand,
            text="Monitorías y Tutorías",
            font=("Segoe UI", 12, "bold"),
            text_color=Colors.TEXT_WHITE,
            anchor="w",
        )
        self.system_name.grid(row=1, column=1, sticky="nw", pady=(0, 17))

        ctk.CTkFrame(self.brand, height=1, fg_color=Colors.PRIMARY_LIGHT).grid(
            row=2, column=0, columnspan=2, sticky="ew", padx=12
        )

    def _build_menu(self) -> None:
        self.menu = SidebarMenu(
            self,
            role=self.current_role,
            callback=self._on_selected,
        )
        self.menu.grid(row=1, column=0, sticky="nsew", padx=20, pady=(20, 12))

    def _build_footer(self) -> None:
        self.footer = ctk.CTkFrame(self, fg_color="transparent")
        self.footer.grid(row=2, column=0, sticky="ew")

        # Separador superior
        ctk.CTkFrame(self.footer, height=1, fg_color=Colors.PRIMARY_LIGHT).pack(
            fill="x", padx=0
        )

        # Perfil de usuario
        self.profile = SidebarProfile(self.footer)
        self.profile.pack(fill="x", padx=20, pady=(12, 8))

        # Botón de cerrar sesión en la parte inferior del sidebar
        ctk.CTkFrame(
            self.footer,
            height=1,
            fg_color=Colors.PRIMARY_LIGHT
        ).pack(
            fill="x",
            padx=20,
            pady=(0,12)
        )

        LogoutButton(

            self.footer,

            command=lambda: self.command("logout")

        ).pack(

            fill="x",

            padx=20,

            pady=(0,18)

        )

    def _on_selected(self, option: str) -> None:
        if self.command is not None:
            self.command(option)

    def set_user(self, name: str, role: str) -> None:
        self.current_role = role
        self.profile.set_user(name, role)
        self.menu.load(role)

    def expand(self) -> None:
        if self.expanded:
            return

        self.expanded = True
        self.configure(width=self.EXPANDED_WIDTH)
        self.menu.grid_configure(padx=20)
        self.brand_name.grid()
        self.system_name.grid()
        self.profile.expand()
        self.menu.expand()

    def collapse(self) -> None:
        if not self.expanded:
            return

        self.expanded = False
        self.configure(width=self.COLLAPSED_WIDTH)
        self.menu.grid_configure(padx=14)
        self.brand_name.grid_remove()
        self.system_name.grid_remove()
        self.profile.collapse()
        self.menu.collapse()

    def toggle(self) -> None:
        if self.expanded:
            self.collapse()
        else:
            self.expand()

    def get_current_role(self) -> str:
        return self.current_role

    def get_current_option(self):
        return self.menu.current_option
