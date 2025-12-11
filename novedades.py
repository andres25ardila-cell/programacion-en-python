from producto import Producto

class novedades(Producto):
    def __init__(self, precio, titulo, autor, editorial, año, preferencias, clasificacion, tema):
        super().__init__(precio, titulo, autor, editorial, año, preferencias)
        self.clasificacion = clasificacion
        self.tema = tema
    
    def cambiar_clasificacion(self, clasificacion):
        print(f"La clasificacion ha sido cambiada {clasificacion}")
    