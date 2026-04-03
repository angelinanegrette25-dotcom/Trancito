import random

class Alerta:
    def __init__(self, id_alerta: int, tipo: str, mensaje: str, nivel_riesgo: int):
        self.id_alerta = id_alerta
        self.tipo = tipo # Ejemplo: 'Foto-multa', 'Retén', 'Accidente'
        self.mensaje = mensaje
        self.nivel_riesgo = nivel_riesgo # Del 1 al 5

    def analizar_riesgo_ia(self) -> str:
        # Simulación de IA que predice probabilidad de multa
        probabilidad = (self.nivel_riesgo * 0.15) + random.random()
        if probabilidad > 0.7:
            return "ALTO RIESGO: Se recomienda cambiar de ruta inmediatamente."
        return "Riesgo moderado: Conduzca con precaución."