class Vehiculo:
    def __init__(self, placa, tipo, marca, modelo, color): # Corregido: doble guion bajo
        self.placa = placa
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrar_info(self):
        return (
            f"Vehículo: {self.tipo}\n"
            f"Placa: {self.placa}\n"
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Color: {self.color}"
        )

    def __str__(self): # Corregido: doble guion bajo
        return f"{self.tipo} - {self.placa} ({self.marca} {self.modelo})"