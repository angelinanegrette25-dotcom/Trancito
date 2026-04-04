import random

class Alerta:
    def __init__(self, id_alerta, tipo, mensaje, ubicacion, nivel_riesgo):
        self.id_alerta = id_alerta
        self.tipo = tipo
        self.mensaje = mensaje
        self.ubicacion = ubicacion
        self.nivel_riesgo = nivel_riesgo

    def analizar_riesgo_ia(self):
        # Simulación de IA predictiva
        probabilidad = (self.nivel_riesgo * 0.15) + random.random()
        return round(min(probabilidad * 100, 100), 2)

    def __str__(self):
        return f"[ALERTA {self.id_alerta}] {self.tipo} - Riesgo: {self.nivel_riesgo}"