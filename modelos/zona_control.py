class ZonaControl:
    def __init__(self, id_zona, tipo_control, ubicacion, limite_velocidad):
        self.id_zona = id_zona
        self.tipo_control = tipo_control
        self.ubicacion = ubicacion
        self.limite_velocidad = limite_velocidad

    def mostrar_info(self):
        return (
            f"Zona {self.id_zona}\n"
            f"Tipo: {self.tipo_control}\n"
            f"Ubicación: {self.ubicacion}\n"
            f"Límite: {self.limite_velocidad} km/h"
        )

    def __str__(self):
        return f"{self.tipo_control} en {self.ubicacion}"