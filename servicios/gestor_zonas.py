geopy
colorama
pytest

class GestorZonas:
    def __init__(self):
        self.zonas = []

    def agregar_zona(self, zona):
        self.zonas.append(zona)

    def mostrar_zonas(self):
        if len(self.zonas) == 0:
            return "No hay zonas registradas"

        texto = ""

        for zona in self.zonas:
            texto += str(zona) + "\n"

        return texto