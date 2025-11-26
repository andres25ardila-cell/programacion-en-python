from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico

#Codigo principal
#Aqui va la logica del negocio

#Isntancia del padre
objBotella = Botella("Coca-Cola", "1.5L", "Especial")
#Instancia hija
objBotella_plastica = Botella_plastico ("Pepsi", "500ML", "Comun", "Redondo", "Plastico", "Sin tinte")
dato_out = objBotella_plastica.imprimir_info()
print(dato_out)
 


