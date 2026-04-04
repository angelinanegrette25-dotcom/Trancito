class Usuario:
    def __init__(self, id_usuario, nombre, correo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.vehiculos = []
        self.historial_trayectos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def agregar_trayecto(self, trayecto):
        self.historial_trayectos.append(trayecto)

    def mostrar_vehiculos(self):
        if not self.vehiculos:
            return "El usuario no tiene vehículos registrados."
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)

    def __str__(self):
        return f"Usuario {self.id_usuario}: {self.nombre}"