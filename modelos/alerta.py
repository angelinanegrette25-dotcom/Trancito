import random


class Alerta:
    def __init__(self, id_alerta, tipo, mensaje, ubicacion, nivel_riesgo):
        self.id_alerta = id_alerta
        self.tipo = tipo
        self.mensaje = mensaje
        self.ubicacion = ubicacion
        self.nivel_riesgo = nivel_riesgo

    def analizar_riesgo(self):
        probabilidad = (self.nivel_riesgo * 15) + random.randint(1, 20)

        if probabilidad > 100:
            probabilidad = 100

        return probabilidad

    def __str__(self):
        return f"{self.tipo} - Riesgo {self.nivel_riesgo}"