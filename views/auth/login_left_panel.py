"""
login_left_panel.py
-------------------

Panel izquierdo del Login.
"""

from __future__ import annotations

import customtkinter as ctk

from components.panels.panel import Panel
from components.labels.title_label import TitleLabel
from components.labels.subtitle_label import SubtitleLabel

from utils.image_loader import ImageLoader

from config.colors import Colors
from config.settings import Settings
from config.fonts import Fonts


class LoginLeftPanel(Panel):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=Colors.PRIMARY
        )

        self.logo = None

        self._build()

    # ==================================================
    # Construcción
    # ==================================================

    def _build(self):

        container = self.content

        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=0)
        container.grid_rowconfigure(2, weight=1)

        container.grid_columnconfigure(0, weight=1)

        center = ctk.CTkFrame(
            container,
            fg_color="transparent"
        )

        center.grid(
            row=1,
            column=0,
            padx=60,
            pady=(60, 0),
            sticky=""
        )

        # ============================================
        # Logo
        # ============================================

        self.logo = ImageLoader.load(
            Settings.APP_LOGO,
            (None, Settings.LOGIN_LOGO_HEIGHT)
        )

        logo = ctk.CTkLabel(
            center,
            image=self.logo,
            text=""
        )

        logo.pack(
            pady=(0, 30)
        )

        # ============================================
        # Título
        # ============================================

        ctk.CTkFrame(
            center,
            fg_color=Colors.GOLD,
            height=2
        ).pack(
            fill="x",
            pady=(0, 12)
        )

        title = TitleLabel(
            center,
            text="Monitorías y\nTutorías"
        )

        title.configure(
            text_color=Colors.GOLD,
            justify="center",
            anchor="center"
        )

        title.pack()

        ctk.CTkFrame(
            center,
            fg_color=Colors.GOLD,
            height=2
        ).pack(
            fill="x",
            pady=(12, 24)
        )

        # ============================================
        # Subtítulo
        # ============================================

        subtitle = SubtitleLabel(
            center,
            text=(
                "Sistema institucional para la gestión\n"
                "integral de monitorías y tutorías\n"
                "académicas."
            )
        )

        subtitle.configure(
            text_color="#DCEDEB",
            justify="center"
        )

        subtitle.pack(
            pady=(18, 0)
        )

        # ============================================
        # Frase
        # ============================================

        quote = ctk.CTkLabel(
            center,
            text=(
                '"Aprender Juntos es Avanzar más Lejos"'
            ),
            font=Fonts.BODY,
            justify="center",
            text_color=Colors.GOLD
        )

        quote.pack(
            pady=(36, 0)
        )

        # ============================================
        # Versión
        # ============================================

        version = ctk.CTkLabel(
            container,
            text=f"Versión {Settings.VERSION}",
            font=Fonts.SMALL,
            text_color="#BFD9D5"
        )

        version.grid(
            row=2,
            column=0,
            sticky="s",
            pady=30
        )