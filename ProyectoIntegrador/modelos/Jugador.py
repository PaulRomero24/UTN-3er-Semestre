class Jugador:
    def __init__(self, id_jugador, nombre, password, puntaje=0):
        self.id_jugador = id_jugador  # ✅ nuevo — viene de PostgreSQL
        self.nombre = nombre
        self.password = password      # ✅ nuevo — para el login
        self.puntaje = puntaje

    def __str__(self):
        return f"Jugador(id={self.id_jugador}, nombre='{self.nombre}', puntaje={self.puntaje})"