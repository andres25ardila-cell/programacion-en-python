class Editorial:
    
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        
    def vender(self):
        print(f"El producto ha sido vendido al editorial {self.nombre}")