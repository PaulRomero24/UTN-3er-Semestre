import psycopg2 as bd

class Conexion:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conn = None    

    def obtener_conexion(self):
        if self.conn is None:
            try:
                self.conn = bd.connect(
                    host=self.host,
                    port=self.port,
                    database=self.database,
                    user=self.user,
                    password=self.password
                )
                print("✅ Conexión a la base de datos establecida.")
            except Exception as e:
                print(f"Error al conectar a la base de datos: {e}")
                self.conn = None
        return self.conn

    def cerrar_conexion(self):
        if self.conn:
            try:
                self.conn.close()
                self.conn = None
                print("✅ Conexión cerrada.")
            except Exception as e:
                print(f"Error al cerrar la conexión: {e}")

    def obtener_Cursor(self):
        if self.conn:
            try:
                return self.conn.cursor()
            except Exception as e:
                print(f"Error al obtener el cursor: {e}")
                return None
        else:
            print("No hay conexión disponible.")
            return None

    def cerrar_Cursor(self, cursor):
        if cursor:
            try:
                cursor.close()
            except Exception as e:
                print(f"Error al cerrar el cursor: {e}")