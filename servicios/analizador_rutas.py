class AnalizadorRutas:
    def analizar_ruta(self, ruta, zonas):
        alertas = []

        for punto in ruta.puntos:

            for zona in zonas:

                distancia = punto.calcular_distancia(
                    zona.ubicacion
                )

                if distancia <= 1:
                    alertas.append(
                        f"Alerta cerca de {zona.tipo_control}"
                    )

        return alertas