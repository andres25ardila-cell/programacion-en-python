class Usuario:
    def __init__(self, nombre, apellido, n_de_cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.n_de_cuenta = n_de_cuenta
        self.direccion = direccion
        self.login = login
        self.password = password
        
    def enviar_sugerencia(self):
        print(f"El usuario {self.nombre} {self.apellido} ha enviado una sugerencia")
        
    def leer(self):
        print(f"El usuario {self.nombre} {self.apellido} está leyendo un revista")
        
    def comprar(self):
        print(f"El usuario {self.nombre} {self.apellido} acaba de comprar un libro")
        
    def vender(self):
        print(f"Se le ha vendido un producto al usuario {self.nombre} {self.apellido}")
        
    def realizar_reclamación(self):
        print(f"El usuario {self.nombre} {self.apellido} esta haciendo una reclamación")