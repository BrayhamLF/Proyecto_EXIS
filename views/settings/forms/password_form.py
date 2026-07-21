"""
password_form.py
----------------

Formulario para actualizar la contraseña.
"""

from __future__ import annotations

import customtkinter as ctk

from components.fields.password_entry import PasswordEntry
from components.buttons.primary_button import PrimaryButton

from config.colors import Colors
from config.fonts import Fonts


class PasswordForm(ctk.CTkFrame):

    def __init__(
        self,
        master,
        command=None,
        logout_callback=None
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        # command: function to perform password update. Should return truthy on success.
        self.command = command

        # Optional callback to perform logout (navegación al login)
        self.logout_callback = logout_callback

        self.current_password = None
        self.new_password = None
        self.confirm_password = None

        self.message = None
        self.submit_button = None

        self._build()

    # ==================================================
    # Construcción
    # ==================================================

    def _build(self):

        self.grid_columnconfigure(0, weight=1)

        # -------------------------------------------------
        # Contraseña actual
        # -------------------------------------------------

        self.current_password = PasswordEntry(

            self,

            label="Contraseña actual",

            placeholder="Ingrese la contraseña actual"

        )

        self.current_password.grid(

            row=0,

            column=0,

            sticky="ew",

            pady=(0, 28)

        )

        # -------------------------------------------------
        # Nueva contraseña
        # -------------------------------------------------

        self.new_password = PasswordEntry(

            self,

            label="Nueva contraseña",

            placeholder="Ingrese la nueva contraseña"

        )

        self.new_password.grid(

            row=1,

            column=0,

            sticky="ew",

            pady=(0, 16)

        )

        # -------------------------------------------------
        # Confirmación
        # -------------------------------------------------

        self.confirm_password = PasswordEntry(

            self,

            label="Confirmar nueva contraseña",

            placeholder="Repita la nueva contraseña"

        )

        self.confirm_password.grid(

            row=2,

            column=0,

            sticky="ew",

            pady=(0, 8)

        )

        # -------------------------------------------------
        # Mensaje
        # -------------------------------------------------

        self.message = ctk.CTkLabel(

            self,

            text="",

            anchor="w",

            justify="left",

            font=Fonts.SMALL,

            text_color=Colors.ERROR

        )

        self.message.grid(

            row=3,

            column=0,

            sticky="ew",

            pady=(0, 10)

        )

        # ------------------------------------------------
        # Acciones
        # ------------------------------------------------

        actions = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        actions.grid(
            row=4,
            column=0,
            sticky="ew",
            pady=(10, 0)
        )

        actions.grid_columnconfigure(0, weight=1)
        actions.grid_columnconfigure(1, weight=0)
        actions.grid_columnconfigure(2, weight=1)

        self.submit_button = PrimaryButton(
            actions,
            text="Actualizar contraseña",
            command=self._submit,
            width=260
        )

        self.submit_button.grid(
            row=0,
            column=1,
            pady=(0, 10)
        )

    # ==================================================
    # Eventos
    # ==================================================

    def _submit(self):
        
        self.set_disabled()
        
        if not self.validate():
            return

        # Ejecutar comando de actualización si existe y manejar resultado
        result = True

        if callable(self.command):

            try:
                result = self.command(
                    self.get_values()
                )
            except Exception as exc:
                # Mostrar error genérico
                self.show_message(
                    "Error al actualizar la contraseña. Intente de nuevo."
                )
                
                self.set_enabled()
                
                return

        # Si el comando no devuelve nada (None), considerarlo éxito
        if result is None:
            result = True

        # Si la operación fue exitosa
        if result:
            self.show_success("Contraseña actualizada correctamente.")
            # Pedir al usuario que cierre sesión para aplicar el cambio
            self.after(200, self._ask_logout_confirm)
        else:
            # Si el comando devolvió falsy, mostrar mensaje genérico (el comando puede haber mostrado su propio mensaje)
            self.show_message("No se pudo actualizar la contraseña.")
            
            self.set_enabled()

    # ==================================================
    # Validaciones
    # ==================================================

    def validate(self):

        self.clear_message()

        self._clear_field_states()

        return (

            self._validate_current_password()

            and

            self._validate_new_password()

            and

            self._validate_confirmation()

            and

            self._validate_password_policy()

            and

            self._validate_match()

        )

    def _validate_current_password(self):

        if self.current_password.is_empty():

            self.current_password.set_error()

            self.show_message(
                "Ingrese la contraseña actual."
            )

            self.current_password.focus()

            return False

        return True

    def _validate_new_password(self):

        if self.new_password.is_empty():

            self.new_password.set_error()

            self.show_message(
                "Ingrese la nueva contraseña."
            )

            self.new_password.focus()

            return False

        return True

    def _validate_confirmation(self):

        if self.confirm_password.is_empty():

            self.confirm_password.set_error()

            self.show_message(
                "Confirme la nueva contraseña."
            )

            self.confirm_password.focus()

            return False

        return True

    def _validate_password_policy(self):

        """
        Futuras validaciones:

        • Longitud mínima
        • Mayúsculas
        • Minúsculas
        • Número
        • Carácter especial
        """

        return True

    def _validate_match(self):

        if (

            self.new_password.get()

            !=

            self.confirm_password.get()

        ):

            self.new_password.set_error()

            self.confirm_password.set_error()

            self.show_message(
                "Las contraseñas no coinciden."
            )

            return False

        self.current_password.set_success()
        self.new_password.set_success()
        self.confirm_password.set_success()

        return True

    # ==================================================
    # Estados
    # ==================================================

    def _clear_field_states(self):

        self.current_password.clear_error()

        self.new_password.clear_error()

        self.confirm_password.clear_error()

    # ==================================================
    # Mensajes
    # ==================================================

    def show_message(
        self,
        text,
        color=Colors.ERROR
    ):

        self.message.configure(
            text=text,
            text_color=color
        )

    def show_success(self, text):

        self.show_message(
            text,
            Colors.SUCCESS
        )

    def clear_message(self):

        self.message.configure(
            text=""
        )
    
    

    # ==================================================
    # API
    # ==================================================

    def get_values(self):

        return {

            "current_password": self.current_password.get(),

            "new_password": self.new_password.get(),

            "confirm_password": self.confirm_password.get()

        }

    def clear(self):

        self.current_password.clear()

        self.new_password.clear()

        self.confirm_password.clear()

        self.clear_message()

        self._clear_field_states()

    # ==================================================
    # Confirmación de logout
    # ==================================================

    def _ask_logout_confirm(self):
        """
        Muestra un diálogo modal solicitando al usuario cerrar sesión
        para aplicar el cambio de contraseña. Al confirmar se ejecuta
        el logout_callback si está definido, o se busca un ancestro
        con método `logout()` y se invoca.
        """

        dialog = ctk.CTkToplevel(self)
        dialog.title("Cerrar sesión")
        dialog.geometry("460x190")
        dialog.resizable(False, False)
        dialog.transient(self)
        dialog.grab_set()

        frame = ctk.CTkFrame(dialog, fg_color=Colors.BACKGROUND)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        lbl = ctk.CTkLabel(
            frame,
            text=(
                "Su contraseña ha sido actualizada correctamente.\n\n"
                "Por motivos de seguridad es necesario iniciar sesión nuevamente para aplicar el cambio.\n\n"
                "¿Desea cerrar la sesión ahora?"
            ),
            justify="left",
            anchor="w",
            font=Fonts.BODY,
            text_color=Colors.TEXT
        )
        lbl.pack(fill="x", pady=(0, 12))

        btns = ctk.CTkFrame(frame, fg_color="transparent")
        btns.pack(fill="x", pady=(6, 0))

        def _on_confirm():
            
            dialog.destroy()

            self.clear()

            self._perform_logout()

        def _on_cancel():
           
            dialog.destroy()

            self.clear()

            self.set_enabled()
            
        btn_confirm = ctk.CTkButton(
            btns,
            text="Confirmar",
            fg_color=Colors.PRIMARY_DARK,
            hover_color=Colors.PRIMARY_HOVER,
            text_color=Colors.TEXT_WHITE,
            command=_on_confirm
        )
        btn_confirm.pack(side="right", padx=(6, 0))

        btn_cancel = ctk.CTkButton(
            btns,
            text="Cancelar",
            fg_color=Colors.TRANSPARENT,
            text_color=Colors.TEXT,
            command=_on_cancel
        )
        btn_cancel.pack(side="right")

    def _perform_logout(self):
        # Preferir callback explícito
        if callable(self.logout_callback):
            try:
                self.logout_callback()
                return
            except Exception:
                pass

        # Buscar ancestro con método logout
        host = self._find_logout_host()
        if host is not None and hasattr(host, "logout") and callable(host.logout):
            try:
                host.logout()
            except Exception:
                # No forzar más acciones
                return

    def _find_logout_host(self):
        """Recorre la cadena de padres hasta encontrar un widget con logout()."""
        parent = self.master
        while parent is not None:
            if hasattr(parent, "logout") and callable(getattr(parent, "logout")):
                return parent
            # algunos widgets usan .master o .parent; intentar ambas
            parent = getattr(parent, "master", None)
        return None

    def reset(self):

        self.clear()

    def set_enabled(self):

        self.current_password.enable()

        self.new_password.enable()

        self.confirm_password.enable()

        self.submit_button.configure(
            state="normal"
        )

    def set_disabled(self):

        self.current_password.disable()

        self.new_password.disable()

        self.confirm_password.disable()

        self.submit_button.configure(
            state="disabled"
        )