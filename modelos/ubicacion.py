from geopy.distance import geodesic


class Ubicacion:
    def __init__(self, latitud, longitud, direccion):
        self.latitud = latitud
        self.longitud = longitud
        self.direccion = direccion

    def calcular_distancia(self, otra_ubicacion):
        punto_1 = (self.latitud, self.longitud)
        punto_2 = (otra_ubicacion.latitud, otra_ubicacion.longitud)

        return geodesic(punto_1, punto_2).kilometers

    def __str__(self):
        return self.direccion