class Vehiculo:
    def __init__(self, placa, tipo, marca, modelo, color):
        self.placa = placa
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrar_info(self):
        return (
            f"Placa: {self.placa}\n"
            f"Tipo: {self.tipo}\n"
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Color: {self.color}"
        )

    def __str__(self):
        return f"{self.tipo} {self.marca} - {self.placa}"