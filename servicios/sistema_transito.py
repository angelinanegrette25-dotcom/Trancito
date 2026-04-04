from modelos.trayecto import Trayecto
from modelos.alerta import Alerta


class SistemaTransitoInteligente:
    def _init_(self):
        self.usuarios = []
        self.trayectos = []
        self.alertas = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario_por_id(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def registrar_vehiculo_a_usuario(self, id_usuario, vehiculo):
        usuario = self.buscar_usuario_por_id(id_usuario)
        if usuario:
            usuario.agregar_vehiculo(vehiculo)
            return True
        return False

    def iniciar_trayecto(self, id_trayecto, usuario, vehiculo, ruta):
        trayecto = Trayecto(id_trayecto, usuario, vehiculo, ruta)
        self.trayectos.append(trayecto)
        usuario.agregar_trayecto(trayecto)
        return trayecto

    def generar_alerta(self, id_alerta, tipo, mensaje, ubicacion, nivel_riesgo, trayecto):
        alerta = Alerta(id_alerta, tipo, mensaje, ubicacion, nivel_riesgo)
        self.alertas.append(alerta)
        trayecto.agregar_alerta(alerta)
        return alerta

    def mostrar_usuarios(self):
        if not self.usuarios:
            return "No hay usuarios registrados."

        texto = ""
        for usuario in self.usuarios:
            texto += f"{usuario}\n"
            texto += "Vehículos:\n"

            if usuario.vehiculos:
                for vehiculo in usuario.vehiculos:
                    texto += f"  - {vehiculo}\n"
            else:
                texto += "  - No tiene vehículos registrados.\n"

            texto += "\n"

        return texto


    def mostrar_trayectos(self):
        if not self.trayectos:
            return "No hay trayectos registrados."

        texto = ""
    
        for trayecto in self.trayectos:
            texto += str(trayecto) + "\n"
    
        return texto