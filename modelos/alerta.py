import random


class Alerta:
    def __init__(self, tipo, mensaje, nivel_riesgo):
        self.tipo = tipo
        self.mensaje = mensaje
        self.nivel_riesgo = nivel_riesgo

    def calcular_riesgo(self):
        riesgo = self.nivel_riesgo * 20 + random.randint(0, 10)

        if riesgo > 100:
            riesgo = 100

        return riesgo

    def __str__(self):
        return f"{self.tipo}: {self.mensaje} - Riesgo {self.calcular_riesgo()}%"