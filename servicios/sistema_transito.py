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

        if usuario:
            usuario.agregar_vehiculo(vehiculo)

            return True

        return False

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
        id_alerta,
        tipo,
        mensaje,
        ubicacion,
        nivel_riesgo,
        trayecto
    ):

        alerta = Alerta(
            id_alerta,
            tipo,
            mensaje,
            ubicacion,
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

        return texto