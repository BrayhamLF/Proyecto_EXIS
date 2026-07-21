"""Campo de correo institucional reutilizable."""

from __future__ import annotations

from components.fields.base_entry import BaseEntry


class EmailEntry(BaseEntry):
    def __init__(
        self,
        master,
        label: str = "Correo institucional",
        placeholder: str = "correo@unitropico.edu.co",
        required: bool = True,
    ):
        super().__init__(
            master,
            label=label,
            placeholder=placeholder,
            required=required,
        )

    def validate(self) -> bool:
        if not super().validate():
            return False

        value = self.get().strip()
        if value and not self.EMAIL_PATTERN.fullmatch(value):
            self.show_error("Ingrese un correo electrónico válido.")
            self.set_error_state()
            return False

        return True
