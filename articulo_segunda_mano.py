from producto import Producto

class articulo_segunda_mano(Producto):
    def __init__(self, precio, titulo, autor, editorial, año, preferencias, clasificacion, tema, vendedor):
        super().__init__(precio, titulo, autor, editorial, año, preferencias)
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor