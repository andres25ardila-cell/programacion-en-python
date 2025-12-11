class Producto:
    def __init__(self, precio, titulo, autor, editorial, año, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor 
        self.editorial = editorial
        self.año_de_edicion = año
        self.preferencias = preferencias
    
    def vender(self):
        print(f"El libro se vendió en un precio de: {self.precio}")
        
    def comprar(self):
        print(f"El usuario compró un libro en un precio de: {self.precio}")
        
    def ver_catálogo(self):
        print(f"El usuario ve el catálogo por año de edición {self.año_de_edicion}")