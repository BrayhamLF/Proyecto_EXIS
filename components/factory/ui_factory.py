"""
ui_factory.py
-------------

Fábrica oficial de componentes visuales.
"""

from __future__ import annotations

from components.buttons.primary_button import PrimaryButton
from components.buttons.secondary_button import SecondaryButton

from components.labels.title_label import TitleLabel
from components.labels.subtitle_label import SubtitleLabel

from components.cards.base_card import BaseCard

from components.fields.email_field import EmailEntry
from components.fields.password_entry import PasswordEntry
from components.fields.combo_box import ComboBox


class UIFactory:

    # ==========================================
    # BOTONES
    # ==========================================

    @staticmethod
    def primary_button(parent, text, command=None):

        return PrimaryButton(
            parent,
            text=text,
            command=command
        )

    @staticmethod
    def secondary_button(parent, text, command=None):

        return SecondaryButton(
            parent,
            text=text,
            command=command
        )

    # ==========================================
    # LABELS
    # ==========================================

    @staticmethod
    def title(parent, text):

        return TitleLabel(
            parent,
            text=text
        )

    @staticmethod
    def subtitle(parent, text):

        return SubtitleLabel(
            parent,
            text=text
        )

    # ==========================================
    # INPUTS
    # ==========================================

    @staticmethod
    def email(parent):

        return EmailEntry(parent)

    @staticmethod
    def password(parent):

        return PasswordEntry(parent)

    @staticmethod
    def role(parent):

        return ComboBox(parent)

    # ==========================================
    # TARJETAS
    # ==========================================

    @staticmethod
    def card(parent, **kwargs):

        return BaseCard(
            parent,
            **kwargs
        )