"""
sidebar_profile.py
------------------
"""

from __future__ import annotations

import customtkinter as ctk

from config.colors import Colors
from config.fonts import Fonts


class SidebarProfile(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.avatar = ctk.CTkLabel(
            self,
            text="A",
            width=38,
            height=38,
            corner_radius=19,
            fg_color=Colors.SECONDARY,
            font=Fonts.BODY_BOLD
        )

        self.avatar.pack(
            side="left",
            padx=(0,10)
        )

        info = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        info.pack(
            side="left",
            fill="x",
            expand=True
        )

        self.user = ctk.CTkLabel(
            info,
            text="Administrador",
            font=Fonts.BODY_BOLD,
            text_color=Colors.TEXT_WHITE
        )

        self.user.pack(anchor="w")

        self.role = ctk.CTkLabel(
            info,
            text="ADMINISTRADOR",
            font=Fonts.SMALL,
            text_color=Colors.PRIMARY_SOFT
        )

        self.role.pack(anchor="w")

    # ======================================

    def set_user(self, name, role):

        # Defensive: name or role can be empty or None. Use sensible defaults
        display_name = name or "Usuario"
        display_role = (role or "").upper()
        initial = display_name[0].upper() if display_name else ""

        self.avatar.configure(
            text=initial
        )

        self.user.configure(
            text=display_name
        )

        self.role.configure(
            text=display_role
        )

    # ======================================

    def collapse(self):

        self.user.pack_forget()

        self.role.pack_forget()

    # ======================================

    def expand(self):

        self.user.pack(anchor="w")

        self.role.pack(anchor="w")