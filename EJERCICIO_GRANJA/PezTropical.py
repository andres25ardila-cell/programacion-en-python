from animal import Animal
class PezTropical(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,
                 salinidad, tipo_aleta, de_arrecife):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.salinidad = salinidad
        self.tipo_aleta = tipo_aleta
        self.de_arrecife = de_arrecife

    def nadar(self):
        print(f"{self.nombre} nada entre corales suavemente.")

    def camuflarse(self):
        print(f"{self.nombre} cambia su color para mezclarse.")