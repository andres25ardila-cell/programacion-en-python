#vehiculo.py

class Vehiculo:
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

    # Métodos
    def arranque(self):
        return "El vehículo ha arrancado."

    def apagado(self):
        return "El vehículo está apagado."

    def aceleracion_frenado(self):
        return "Puede acelerar y frenar normalmente."

    def sistema_direccion(self):
        return "Cuenta con dirección estándar."

    def climatizacion(self):
        return "Sistema de aire acondicionado básico."

    def tipo_seguridad(self):
        return "Incluye cinturones y airbags estándar."

    def luces(self):
        return "Luces delanteras y traseras operativas."

    def sistema_ventanas(self):
        return "Ventanas manuales o eléctricas según el modelo."

    def sistema_espejos(self):
        return "Espejos ajustables según el modelo."

    def descripcion(self):
        return f"Vehículo {self.modelo} color {self.color}, motor {self.motor}."