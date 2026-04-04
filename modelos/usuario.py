class Usuario:
    def __init__(self, id_usuario, nombre, correo): 
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
        # Esto llama al __str__ de cada objeto Vehiculo
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)

    def __str__(self): # Corregido: __str__
        return f"Usuario {self.id_usuario}: {self.nombre}"