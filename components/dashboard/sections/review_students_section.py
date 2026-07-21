"""
review_students_section.py
--------------------------

Panel de estudiantes pendientes por revisar.
"""

from __future__ import annotations

from components.panels.admin_panel import AdminPanel

from components.dashboard.widgets.empty_state import EmptyState

from components.lists.list import List
from components.lists.student_item import StudentItem

from utils.icons import Icons


class ReviewStudentsSection(AdminPanel):

    def __init__(self, master):

        super().__init__(
            master,
            title="Estudiantes por revisar",
            badge="0",
            height=320
        )

        # Datos

        self.students = []

        # Componentes

        self.student_list = None
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

        self.student_list = List(body)

        self.student_list.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

    # ==========================================================
    # Datos temporales
    # ==========================================================

    def _load_demo(self):

        self.students = [

            {
                "id": 1,
                "name": "Juan Pérez",
                "program": "Ingeniería de Sistemas",
                "semester": "IX Semestre",
                "status": "Pendiente"
            },

            {
                "id": 2,
                "name": "Laura Gómez",
                "program": "Ingeniería Civil",
                "semester": "VIII Semestre",
                "status": "Pendiente"
            },

            {
                "id": 3,
                "name": "Carlos Ruiz",
                "program": "Ingeniería Ambiental",
                "semester": "VII Semestre",
                "status": "Pendiente"
            }

        ]

        self.refresh()

    # ==========================================================
    # API
    # ==========================================================

    def set_students(
        self,
        students: list[dict]
    ):

        self.students = students

        self.refresh()

    # ==========================================================
    # Actualizar panel
    # ==========================================================

    def refresh(self):

        self.set_badge(
            len(self.students)
        )

        # -------------------------
        # Limpiar lista
        # -------------------------

        self.student_list.clear()

        # -------------------------
        # Sin estudiantes
        # -------------------------

        if not self.students:

            self.student_list.grid_remove()

            if self.empty_state is None:

                self.empty_state = EmptyState(

                    self.get_body(),

                    icon=Icons.students((48, 48)),

                    title="No hay estudiantes",

                    description=(
                        "Actualmente no existen estudiantes "
                        "pendientes por revisar."
                    )

                )

                self.empty_state.grid(
                    row=0,
                    column=0,
                    sticky="nsew"
                )

            return

        # -------------------------
        # Eliminar EmptyState
        # -------------------------

        if self.empty_state is not None:

            self.empty_state.destroy()

            self.empty_state = None

        self.student_list.grid()

        # -------------------------
        # Agregar estudiantes
        # -------------------------

        for student in self.students:

            self.student_list.add_item(

                StudentItem(

                    self.student_list,

                    student_id=student["id"],

                    name=student["name"],

                    program=student["program"],

                    semester=student["semester"],

                    status=student["status"],

                    command=lambda s=student: self._open_student(s)

                )

            )

    # ==========================================================
    # Eventos
    # ==========================================================

    def _open_student(
        self,
        student: dict
    ):

        """
        Posteriormente abrirá la ficha del estudiante.
        """

        print(student)