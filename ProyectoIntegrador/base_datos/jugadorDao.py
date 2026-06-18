from  modelos.Jugador import Jugador

class JugadorDao:
    def __init__(self, db):
        self.db = db

    def registrar_jugador(self, nombre, password):
        """Registra un jugador nuevo en la BD y lo devuelve como objeto"""
        cursor = self.db.obtener_Cursor()
        if cursor:
            try:
                cursor.execute(
                    "INSERT INTO jugadores (nombre, password) VALUES (%s, %s) RETURNING id_jugador",
                    (nombre, password)
                )
                id_jugador = cursor.fetchone()[0]  # ✅ RETURNING devuelve el id generado
                self.db.conn.commit()
                self.db.cerrar_Cursor(cursor)
                print(f"\n✅ Jugador '{nombre}' registrado exitosamente.")
                return Jugador(id_jugador=id_jugador, nombre=nombre, password=password)
            except Exception as e:
                self.db.conn.rollback()
                print(f"Error al registrar jugador: {e}")
                return None
        return None

    def buscar_jugador(self, nombre, password):
        """Busca un jugador por nombre y password, devuelve objeto Jugador o None"""
        cursor = self.db.obtener_Cursor()
        if cursor:
            try:
                cursor.execute(
                    "SELECT id_jugador, nombre, password FROM jugadores WHERE nombre = %s AND password = %s",
                    (nombre, password)
                )
                fila = cursor.fetchone()
                self.db.cerrar_Cursor(cursor)
                if fila:
                    return Jugador(id_jugador=fila[0], nombre=fila[1], password=fila[2])
                return None
            except Exception as e:
                self.db.conn.rollback()
                print(f"Error al buscar jugador: {e}")
                return None
        return None