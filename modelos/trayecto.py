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
        texto = (
            f"Trayecto: {self.id_trayecto}\n"
            f"Usuario: {self.usuario.nombre}\n"
            f"Vehiculo: {self.vehiculo.placa}\n"
            f"Ruta: {self.ruta.origen} -> {self.ruta.destino}\n"
            f"Estado: {self.estado}\n"
        )

        if len(self.alertas) > 0:
            texto += "\nAlertas:\n"

            for alerta in self.alertas:
                riesgo = alerta.analizar_riesgo()

                texto += (
                    f"- {alerta.tipo} "
                    f"({riesgo}% de riesgo)\n"
                )

        return texto

    def __str__(self):
        return f"Trayecto {self.id_trayecto}"