class Trayecto:
    def __init__(self, id_trayecto, usuario, vehiculo, ruta): 
        self.id_trayecto = id_trayecto
        self.usuario = usuario
        self.vehiculo = vehiculo
        self.ruta = ruta
        self.alertas = []
        self.estado = "En curso"

    def agregar_alerta(self, alerta):
        self.alertas.append(alerta)

    def finalizar_trayecto(self):
        self.estado = "Finalizado"

    def mostrar_resumen(self):
        # Usamos nombre_ruta para que coincida con tu clase Ruta
        texto = (
            f"--- RESUMEN TRAYECTO {self.id_trayecto} ---\n"
            f"Usuario: {self.usuario.nombre}\n"
            f"Vehículo: {self.vehiculo.placa}\n"
            f"Ruta: {self.ruta.nombre_ruta}\n"
            f"Estado: {self.estado}\n"
            f"Cantidad de alertas: {len(self.alertas)}\n"
            )

        if self.alertas:
            texto += "Alertas generadas:\n"
            for alerta in self.alertas:
                texto += f"- {alerta.tipo}: {alerta.mensaje}\n"

        return texto

    def _str_(self):
        return f"Trayecto {self.id_trayecto} - {self.estado}"