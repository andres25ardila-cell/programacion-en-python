from producto import Producto

class articulo_online(Producto):
    def __init__(self, precio, titulo, autor, editorial, año, preferencias, tema):
        super().__init__(precio, titulo, autor, editorial, año, preferencias)
        self.tema = tema
        
    def publicar(self):
        print(f"Se ha publicado el tema {self.tema}")