from peliculas import Peliculas
from catalogo_peliculas import CatalogoPelicula

while True:
    print("\n--- MENÚ ---")
    print("1) Agregar película")
    print("2) Listar películas")
    print("3) Eliminar archivos de películas")
    print("4) Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la película: ")#se crea un objeto de la clase Peliculas con el nombre ingresado(metodo de instancia)
        #y se agrega al catálogo usando el método de clase estatico agregar_pelicula, que escribe la película en el archivo de texto.   
        CatalogoPelicula.agregar_pelicula(Peliculas(nombre))
    elif opcion == "2":
        CatalogoPelicula.listar_peliculas()
    elif opcion == "3":
        CatalogoPelicula.eliminar()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")
        
# El proyecto funciona correctamente, se pueden agregar películas, listarlas y eliminar el archivo.
# Se trabaja sobre metodos staticos, lo que hace que no sea necesario crear un objeto de la clase CatalogoPelicula para usar sus métodos.
# Sino que se trabajo sobre le archivo de texto directamente.Se llaman directamente desde la clase, sin crear objetos de la clase CatalogoPelicula.