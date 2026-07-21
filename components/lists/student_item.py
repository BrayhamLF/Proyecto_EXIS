"""
student_item.py
---------------

Elemento visual reutilizable para representar un estudiante
en listas del Dashboard y los módulos del sistema.
"""

from __future__ import annotations

from components.lists.list_item import ListItem
from components.ui.icon_circle import IconCircle
from components.ui.status_badge import StatusBadge

from config.colors import Colors

from utils.icons import Icons


class StudentItem(ListItem):

    STATUS_COLORS = {

        "Pendiente": (
            Colors.WARNING_BG,
            Colors.WARNING
        ),

        "Revisado": (
            Colors.SUCCESS_BG,
            Colors.SUCCESS
        ),

        "Activo": (
            Colors.SUCCESS_BG,
            Colors.SUCCESS
        ),

        "Inactivo": (
            Colors.ERROR_BG,
            Colors.ERROR
        )

    }

    def __init__(
        self,
        master,
        student_id: int,
        name: str,
        program: str,
        semester: str,
        status: str = "Pendiente",
        command=None
    ):

        self.student_id = student_id

        self.name = name

        self.program = program

        self.semester = semester

        self.current_status = status

        super().__init__(
            master,
            title=name,
            subtitle=f"{program} • {semester}",
            command=command
        )

        self._build_avatar()

        self._build_status()

    # =====================================================
    # Avatar
    # =====================================================

    def _build_avatar(self):

        self.avatar = IconCircle(

            self.leading_frame,

            image=Icons.students((18, 18)),

            size=42,

            color=Colors.PRIMARY

        )

        self.avatar.pack(
            expand=True
        )

    # =====================================================
    # Estado
    # =====================================================

    def _build_status(self):

        fg, text = self.STATUS_COLORS.get(

            self.current_status,

            (
                Colors.WARNING_BG,
                Colors.WARNING
            )

        )

        self.status_badge = StatusBadge(

            self.trailing_frame,

            text=self.current_status,

            fg_color=fg,

            text_color=text

        )

        self.status_badge.pack()
    
    # =====================================================
    # API
    # =====================================================

    def set_status(self, status: str):

        self.current_status = status

        fg, text = self.STATUS_COLORS.get(

            status,

            (
                Colors.WARNING_BG,
                Colors.WARNING
            )

        )

        self.status_badge.configure(

            text=status,

            fg_color=fg,

            text_color=text

        )

    def get_student(self):

        return {

            "id": self.student_id,

            "name": self.name,

            "program": self.program,

            "semester": self.semester,

            "status": self.current_status

        }