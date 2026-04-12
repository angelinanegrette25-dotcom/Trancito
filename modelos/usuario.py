class Usuario:
    def __init__(self, id_usuario, nombre, correo, contraseña):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.vehiculos = []
        self.historial_trayectos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def agregar_trayecto(self, trayecto):
        self.historial_trayectos.append(trayecto)

    def mostrar_vehiculos(self):
        if len(self.vehiculos) == 0:
            return "No tiene vehículos"

        texto = ""

        for vehiculo in self.vehiculos:
            texto += str(vehiculo) + "\n"

        return texto

    def __str__(self):
        return f"{self.nombre} - {self.correo}"