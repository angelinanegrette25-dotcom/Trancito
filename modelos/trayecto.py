
class Trayecto:
    def __init__(self, id_trayecto, usuario, vehiculo, ruta):
        self.id_trayecto = id_trayecto
        self.usuario = usuario
        self.vehiculo = vehiculo
        self.ruta = ruta
        self.alertas = []
        self.estado = "En curso"

    def agregar_alerta(self, alerta):
        # Relación de agregación: un trayecto puede tener múltiples alertas
        self.alertas.append(alerta)

    def finalizar_trayecto(self):
        self.estado = "Finalizado"

    def mostrar_resumen(self):
        # Accedemos a los atributos de los objetos relacionados (usuario, vehiculo, ruta)
        texto = (
            f"\n==============================\n"
            f"   RESUMEN DEL TRAYECTO {self.id_trayecto}\n"
            f"==============================\n"
            f"Conductor: {self.usuario.nombre}\n"
            f"Vehículo: {self.vehiculo.placa} ({self.vehiculo.marca})\n"
            f"Recorrido: {self.ruta.origen} -> {self.ruta.destino}\n"
            f"Distancia: {self.ruta.distancia_km} km\n"
            f"Estado actual: {self.estado}\n"
            f"------------------------------\n"
        )

        if self.alertas:
            texto += f"ALERTAS DETECTADAS ({len(self.alertas)}):\n"
            for alerta in self.alertas:
                # Usamos el método de IA predictiva de la clase Alerta
                prob = alerta.analizar_riesgo_ia()
                texto += f"- [{alerta.tipo}] {alerta.mensaje} (Riesgo IA: {prob}%)\n"
        else:
            texto += "No se generaron alertas en este trayecto.\n"
        
        texto += "==============================\n"
        return texto

    def __str__(self):
        return f"Trayecto {self.id_trayecto} | {self.usuario.nombre} | {self.estado}"