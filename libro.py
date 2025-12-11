from producto import Producto

class libro(Producto):
    def __init__(self, precio, titulo, autor, editorial, año, preferencias, genero):
        super().__init__(precio, titulo, autor, editorial, año, preferencias)
        self.genero = genero