from producto import Producto

class revista(Producto):
    def __init__(self, precio, titulo, autor, editorial, año, preferencias, categoria):
        super().__init__(precio, titulo, autor, editorial, año, preferencias)
        self.categoria = categoria