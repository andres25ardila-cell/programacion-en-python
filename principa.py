from producto import Producto
from libro import libro
from revista import revista
from articulo_segunda_mano import articulo_segunda_mano
from articulo_online import articulo_online
from novedades import novedades
from usuario import Usuario
from editorial import Editorial
from procesador import Procesador
from servidor import Servidor
from indexador import Indexador
from recolector import Recolector
from hilo import Hilo

print("--- Creación de Productos ---")
producto_generico = Producto(20.50, "Cuento Genérico", "Autor Base", "Base Editores", 2020, ["Ficción"])
producto_generico.ver_catálogo()

mi_libro = libro(35.99, "Cien Años de Soledad", "García Márquez", "Editorial Sudamericana", 1967, ["Clásico", "Realismo Mágico"], "Novela")
mi_libro.comprar()

mi_revista = revista(5.00, "Tecnología Hoy", "Equipo Editorial", "TechPress", 2025, ["Tecnología"], "Ciencia")
mi_revista.vender()

art_segunda_mano = articulo_segunda_mano(15.00, "Libro de Cálculo Usado", "Varios Autores", "Pearson", 2010, ["Académico"], "Bueno", "Matemáticas", "Pepe Vendedor")

art_online = articulo_online(0.99, "Guía de Python", "Desarrollador IA", "Self-Published", 2024, ["Programación"], "Lenguajes")
art_online.publicar()

novedad_reciente = novedades(40.00, "El Futuro del AI", "Dra. Smith", "Innovación Press", 2025, ["Ciencia"], "Lanzamiento", "Inteligencia Artificial")
novedad_reciente.cambiar_clasificacion("Top Ventas")


print("\n" + "-"*30)

print("--- Creación de Actores y Sistemas ---")
usuario_activo = Usuario("Ana", "García", "123456", "Calle Falsa 123", "anagarcia", "secreto123")
editorial_socia = Editorial("Planeta", "Av. Siempre Viva 742", "555-1234")
procesador_ventas = Procesador()
servidor_principal = Servidor()
indexador_data = Indexador()
recolector_noticias = Recolector()
hilo_fondo = Hilo()

print("\n" + "-"*30)


print("--- Flujo de Compra ---")
usuario_activo.comprar()
servidor_principal.envia_datos_de_compra()
procesador_ventas.realizar_cobro()
mi_libro.comprar()

print("\n" + "-"*30)

print("--- Flujo de Venta ---")
editorial_socia.vender()
servidor_principal.envia_datos_de_venta()
procesador_ventas.mandar_datos_de_venta()
procesador_ventas.realizar_pago()
mi_revista.vender()

print("\n" + "-"*30)

print("--- Flujo de Sugerencia ---")
usuario_activo.enviar_sugerencia()
servidor_principal.envia_sugerencia()
procesador_ventas.envia_sugerencia_administrador()

print("\n" + "-"*30)

print("--- Flujo de Mantenimiento y Búsqueda ---")
servidor_principal.muestra_pagina()
hilo_fondo.busca_novedades()
recolector_noticias.envia_novedades()

indexador_data.actualiza_almacen()
procesador_ventas.modificar_stock() 
procesador_ventas.actualiza_Catalogo() 

procesador_ventas.realiza_busqueda()
indexador_data.envia_resultado_busqueda()