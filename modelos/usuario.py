class Usuario:
    def __init__(self, id_usuario: int, nombre: str, correo: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.vehiculos = []

    def vincular_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"