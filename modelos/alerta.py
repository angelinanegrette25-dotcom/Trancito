class Alerta:
    def _init_(self, id_alerta, tipo, mensaje, ubicacion, nivel_riesgo):
        self.id_alerta = id_alerta
        self.tipo = tipo
        self.mensaje = mensaje
        self.ubicacion = ubicacion
        self.nivel_riesgo = nivel_riesgo

    def mostrar_alerta(self):
        return (
            f"[ALERTA {self.id_alerta}] {self.tipo}\n"
            f"Mensaje: {self.mensaje}\n"
            f"Ubicación: {self.ubicacion}\n"
            f"Nivel de riesgo: {self.nivel_riesgo}"
        )

    def _str_(self):
        return f"{self.tipo} - {self.mensaje}"
