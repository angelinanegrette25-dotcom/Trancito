from geopy.distance import geodesic

class Ubicacion:
    def __init__(self, latitud, longitud, direccion):
        self.latitud = latitud
        self.longitud = longitud
        self.direccion = direccion

    def calcular_distancia(self, otra_ubicacion):
        # Uso de geopy para distancia real en km
        punto1 = (self.latitud, self.longitud)
        punto2 = (otra_ubicacion.latitud, otra_ubicacion.longitud)
        return geodesic(punto1, punto2).kilometers

    def __str__(self):
        return f"{self.direccion} ({self.latitud}, {self.longitud})"
    