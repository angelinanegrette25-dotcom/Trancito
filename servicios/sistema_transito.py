from modelos.trayecto import Trayecto
from modelos.alerta import Alerta


class SistemaTransito:

    def __init__(self):

        self.usuarios = []
        self.trayectos = []
        self.alertas = []

    def registrar_usuario(self, usuario):

        self.usuarios.append(usuario)

    def buscar_usuario(self, id_usuario):

        for usuario in self.usuarios:

            if usuario.id_usuario == id_usuario:
                return usuario

        return None

    def registrar_vehiculo(self, id_usuario, vehiculo):

        usuario = self.buscar_usuario(id_usuario)

        if usuario is None:
            return False

        usuario.agregar_vehiculo(vehiculo)

        return True

    def crear_trayecto(
        self,
        id_trayecto,
        usuario,
        vehiculo,
        ruta
    ):

        trayecto = Trayecto(
            id_trayecto,
            usuario,
            vehiculo,
            ruta
        )

        self.trayectos.append(trayecto)

        usuario.agregar_trayecto(trayecto)

        return trayecto

    def generar_alerta(
        self,
        tipo,
        mensaje,
        nivel_riesgo,
        trayecto
    ):

        alerta = Alerta(
            tipo,
            mensaje,
            nivel_riesgo
        )

        self.alertas.append(alerta)

        trayecto.agregar_alerta(alerta)

        return alerta

    def mostrar_usuarios(self):

        if len(self.usuarios) == 0:
            return "No hay usuarios"

        texto = ""

        for usuario in self.usuarios:

            texto += str(usuario) + "\n"
            texto += usuario.mostrar_vehiculos() + "\n"

        return texto

    def iniciar_sesion(self, correo, contraseña):

        for usuario in self.usuarios:

            if (
                    usuario.correo == correo
                    and
                    usuario.contraseña == contraseña
            ):
                return usuario

        return None

    