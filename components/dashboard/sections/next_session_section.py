"""
next_session_section.py
-----------------------

Panel de la próxima monitoría o tutoría programada.
"""

from __future__ import annotations

from components.panels.admin_panel import AdminPanel

from components.cards.session_card import SessionCard
from components.dashboard.widgets.empty_state import EmptyState

from utils.icons import Icons


class NextSessionSection(AdminPanel):

    def __init__(self, master):

        super().__init__(
            master,
            title="Próxima sesión",
            badge="1",
            height=320
        )

        # Datos

        self.session = None

        # Componentes

        self.session_card = None
        self.empty_state = None

        self._build()

        self._load_demo()

    # ==========================================================
    # Construcción
    # ==========================================================

    def _build(self):

        body = self.get_body()

        body.grid_rowconfigure(0, weight=1)
        body.grid_columnconfigure(0, weight=1)

    # ==========================================================
    # Datos temporales
    # ==========================================================

    def _load_demo(self):

        self.session = {

            "subject": "Programación II",

            "tutor": "Carlos Pérez",

            "monitor": "Laura Gómez",

            "date": "18 Julio 2026",

            "hour": "08:00 AM - 10:00 AM",

            "location": "Sala 203"

        }

        self.refresh()

    # ==========================================================
    # API
    # ==========================================================

    def set_session(
        self,
        session: dict | None
    ):

        self.session = session

        self.refresh()

    # ==========================================================
    # Actualizar
    # ==========================================================

    def refresh(self):

        body = self.get_body()

        # ------------------------------------------------------
        # Sin sesión
        # ------------------------------------------------------

        if self.session is None:

            if self.session_card is not None:

                self.session_card.destroy()
                self.session_card = None

            if self.empty_state is None:

                self.empty_state = EmptyState(

                    body,

                    icon=Icons.sessions((48, 48)),

                    title="Sin sesión programada",

                    description=(
                        "Actualmente no existe una "
                        "monitoría programada."
                    )

                )

                self.empty_state.grid(
                    row=0,
                    column=0,
                    sticky="nsew"
                )

            self.set_badge("0")

            return

        # ------------------------------------------------------
        # Hay sesión
        # ------------------------------------------------------

        self.set_badge("1")

        if self.empty_state is not None:

            self.empty_state.destroy()
            self.empty_state = None

        if self.session_card is None:

            self.session_card = SessionCard(

                body,

                subject=self.session["subject"],

                tutor=self.session["tutor"],

                monitor=self.session["monitor"],

                date=self.session["date"],

                hour=self.session["hour"],

                location=self.session["location"]

            )

            self.session_card.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

        else:

            self.session_card.update_session(
                self.session
            )