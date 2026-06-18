from utilidades.Ranking import Ranking

class RankingDao:
    def __init__(self, db):
        self.db = db

    def agregar_puntaje(self, id_jugador, puntaje, turnos, resultado):
        """Guarda el resultado de una partida en la BD"""
        cursor = self.db.obtener_Cursor()
        if cursor:
            try:
                cursor.execute(
                    """INSERT INTO ranking (id_jugador, puntaje, turnos, resultado)
                    VALUES (%s, %s, %s, %s)""",
                    (id_jugador, puntaje, turnos, resultado)
                )
                self.db.conn.commit()
                self.db.cerrar_Cursor(cursor)
                print("✅ Puntaje guardado en el ranking.")
            except Exception as e:
                self.db.conn.rollback()
                print(f"Error al guardar puntaje: {e}")

    def obtener_top10(self):
        """Devuelve los 10 mejores puntajes con nombre del jugador"""
        cursor = self.db.obtener_Cursor()
        if cursor:
            try:
                cursor.execute("""
                    SELECT j.nombre, r.puntaje, r.turnos, r.resultado, r.fecha
                    FROM ranking r
                    JOIN jugadores j ON r.id_jugador = j.id_jugador
                    ORDER BY r.puntaje DESC
                    LIMIT 10
                """)
                resultados = cursor.fetchall()
                self.db.cerrar_Cursor(cursor)
                return resultados
            except Exception as e:
                self.db.conn.rollback()
                print(f"Error al obtener ranking: {e}")
                return []
        return []