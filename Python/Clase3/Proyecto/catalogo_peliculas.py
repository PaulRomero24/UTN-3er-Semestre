from peliculas import Peliculas

class CatalogoPelicula:
    ruta_archivo = "peliculas.txt"

    @staticmethod
    def agregar_pelicula(pelicula: Peliculas):
        with open(CatalogoPelicula.ruta_archivo, "a") as f:
            f.write(f"--{pelicula}\n")

    @staticmethod
    def listar_peliculas():
        try:
            with open(CatalogoPelicula.ruta_archivo, "r") as f:
                peliculas = f.readlines()
            for i, p in enumerate(peliculas, 1):
                print(f"{i}. {p.strip()}")
        except FileNotFoundError:
            print("No hay películas registradas.")

    @staticmethod
    def eliminar():
        import os
        if os.path.exists(CatalogoPelicula.ruta_archivo):
            os.remove(CatalogoPelicula.ruta_archivo)
            print("Archivo eliminado.")
        else:
            print("No existe el archivo.")
    
    #Este método muestra el listado de películas registradas en el archivo,
    #si no hay películas registradas o el archivo no existe, muestra un mensaje indicando que no hay películas registradas.
    #Funciona casi igual que el método listar_peliculas, pero en lugar de imprimir las películas, devuelve una lista de las películas registradas.
    
    ##@staticmethod
    ##def mostrar_peliculas():
    ##    try:
    ##       with open(CatalogoPelicula.ruta_archivo, "r") as f:
    ##            peliculas = f.readlines()
    ##            if peliculas:
    ##                return peliculas
    ##           else:
    ##                print("No hay películas registradas.")
    ##            return []
    #   except FileNotFoundError:
    #      print("No hay películas registradas.")
    #     return []