#metodo de instancia: se llama a través de un objeto
#metodo de clase: se llama a través de la clase, no necesita un objeto para ser llamado
class Peliculas:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __str__(self):
        return self.nombre