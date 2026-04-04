
from modelos.trayecto import Trayecto
from modelos.alerta import Alerta

class SistemaTransitoInteligente:
    def __init__(self): 
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
        # Creamos el objeto Trayecto vinculando todas las piezas
        trayecto = Trayecto(id_trayecto, usuario, vehiculo, ruta)
        self.trayectos.append(trayecto)
        # Importante: Guardamos el viaje en el historial del usuario
        usuario.agregar_trayecto(trayecto)
        return trayecto

    def generar_alerta_ia(self, id_alerta, tipo, mensaje, ubicacion, nivel_riesgo, trayecto):
        # Creamos la alerta
        alerta = Alerta(id_alerta, tipo, mensaje, ubicacion, nivel_riesgo)
        
        # Invocamos la funcionalidad IA Predictiva
        probabilidad = alerta.analizar_riesgo_ia()
        alerta.mensaje += f" [Riesgo detectado por IA: {probabilidad}%]"
        
        self.alertas.append(alerta)
        # La alerta se suma al trayecto actual
        trayecto.agregar_alerta(alerta)
        return alerta

    def mostrar_usuarios(self):
        if not self.usuarios:
            return "No hay usuarios registrados."

        texto = "=== REPORTE DE USUARIOS Y FLOTA ===\n"
        for usuario in self.usuarios:
            texto += f"{usuario}\n"
            texto += "Vehículos registrados:\n"
            texto += f"{usuario.mostrar_vehiculos()}\n"
            texto += "-" * 30 + "\n"
        return texto

    def mostrar_trayectos(self):
        if not self.trayectos:
            return "No hay trayectos registrados en el historial."

        texto = "=== HISTORIAL DE TRAYECTOS ACTIVOS ===\n"
        for trayecto in self.trayectos:
            texto += f"{trayecto}\n" # Esto usa el __str__ de Trayecto
        return texto