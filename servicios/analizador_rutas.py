class AnalizadorRutas:
    def analizar_ruta(self, ruta, zonas):
        alertas = []

        for punto in ruta.puntos:
            for zona in zonas:
                distancia = punto.calcular_distancia(zona.ubicacion)

                if distancia <= 1:
                    mensaje = (
                        f"Cerca de {zona.tipo_control}. "
                        f"Límite permitido: {zona.limite_velocidad} km/h"
                    )
                    alertas.append(mensaje)

        return alertas