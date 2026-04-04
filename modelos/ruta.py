
class Ruta:
    def __init__(self, id_ruta: int, nombre_ruta: str):
        self.id_ruta = id_ruta
        self.nombre_ruta = nombre_ruta
        self.puntos = [] # Lista de objetos Ubicacion
    
    def agregar_punto(self, ubicacion):
        self.puntos.append(ubicacion)
        