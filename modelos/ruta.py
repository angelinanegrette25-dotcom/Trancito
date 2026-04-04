
class Ruta:
    def __init__(self, id_ruta, origen, destino, distancia_km): 
        self.id_ruta = id_ruta
        self.origen = origen
        self.destino = destino
        self.distancia_km = distancia_km
        self.puntos = [] # guardarán objetos de la clase Ubicacion

    def agregar_punto(self, ubicacion):
        self.puntos.append(ubicacion)

    def mostrar_ruta(self):
        texto = (
            f"Ruta {self.id_ruta}\n"
            f"Origen: {self.origen}\n"
            f"Destino: {self.destino}\n"
            f"Distancia: {self.distancia_km} km\n"
        )
        if self.puntos:
            texto += "Puntos de la ruta:\n"
            for punto in self.puntos:
                texto += f"- {punto}\n"
        return texto

    def __str__(self): 
        return f"Ruta {self.id_ruta}: {self.origen} -> {self.destino}"