from enum import Enum
from base_datos.Conexion import Conexion
from base_datos.jugadorDao import JugadorDao
from base_datos.RankingDao import RankingDao
from utilidades.Ranking import Ranking
from base_datos.Login import Login
from modelos.tablero import Tablero
from modelos.Jugador import Jugador
from utilidades.Coordenadas import Coordenadas
# =============================================
#           ESTADOS DEL JUEGO
# =============================================
class EstadoJuego(Enum):
    GANADO             = "ganado"
    PERDIDO_SIN_DISPAROS = "perdido"
    RENDIDO            = "rendido"

DISPAROS_TOTALES = 25

# =============================================
#           CONEXIÓN A POSTGRESQL
# =============================================
db = Conexion(
    host="localhost",
    port=5432,
    database="batalla_naval",
    user="postgres",
    password="admin"
)
db.obtener_conexion()

# =============================================
#           INSTANCIAS DE CLASES
# =============================================
jugador_dao = JugadorDao(db)
ranking_dao = RankingDao(db)
ranking     = Ranking(ranking_dao)
login       = Login(jugador_dao)

# =============================================
#           MENU PRINCIPAL
# =============================================
def mostrar_menu():
    print("\n" + "=" * 40)
    print("        BATALLA NAVAL - MENÚ")
    print("=" * 40)
    print("1. Jugar")
    print("2. Ver Ranking")
    print("3. Salir")

def leer_entero():
    try:
        return int(input("Seleccione una opción: ").strip())
    except ValueError:
        return -1

# =============================================
#           LÓGICA DEL JUEGO
# =============================================
def jugar():
    # Login antes de jugar
    jugador = login.iniciar_sesion()
    if not jugador:
        print("Volviendo al menú...")
        return

    puntaje            = 125
    disparos_restantes = DISPAROS_TOTALES
    disparos_validos   = 0
    tablero            = Tablero()
    tablero.colocar_barco()
    estado             = EstadoJuego.PERDIDO_SIN_DISPAROS

    # Bucle principal del juego
    while not tablero.juego_finalizado() and disparos_restantes > 0:
        print()
        tablero.mostrar_vista_jugador()
        print(f"\n Disparos restantes: {disparos_restantes}")
        print(f" Puntaje actual:     {puntaje}")

        # Cada 5 disparos válidos se habilita la opción de rendirse
        if disparos_validos > 0 and disparos_validos % 5 == 0:
            entrada = input("\nIngrese coordenada (ej: A5) o 'salir' para rendirse: ").strip()
            if entrada.lower() in ["salir", "rendirse", "q"]:
                print(f"\n Te has rendido tras {disparos_validos} disparos válidos.")
                estado = EstadoJuego.RENDIDO
                break
        else:
            entrada = input("\nIngrese coordenada (ej: A5): ").strip()

        # Parsear coordenada
        coords = Coordenadas.parsear_coordenada(entrada)
        if coords is None:
            print("\n Formato incorrecto. Usá letra y número (ej: A5).")
            continue

        fila, columna = coords

        # Ejecutar disparo
        if not tablero.disparar(fila, columna):
            print("\n Ya disparaste ahí o la coordenada es inválida.")
            continue

        disparos_validos   += 1
        disparos_restantes -= 1

        # Resultado del disparo
        resultado = tablero.get_vista_jugador()[fila][columna]
        if resultado == 'O':
            puntaje -= 5
            print("\n ¡Agua! (-5 puntos)")
        elif resultado in ['X', '#']:
            print("\n ¡Impacto! 💥")

        if disparos_validos % 5 == 0:
            print(f" Has completado {disparos_validos} disparos válidos.")

    # Determinar estado final
    if tablero.juego_finalizado():
        estado = EstadoJuego.GANADO
    elif estado != EstadoJuego.RENDIDO:
        estado = EstadoJuego.PERDIDO_SIN_DISPAROS

    mostrar_resultado_final(tablero, puntaje, disparos_restantes, estado)

    # Guardar en BD solo si no se rindió
    if estado != EstadoJuego.RENDIDO:
        disparos_usados = DISPAROS_TOTALES - disparos_restantes
        ranking_dao.agregar_puntaje(
            jugador.id_jugador,
            puntaje,
            disparos_usados,
            estado.value
        )

# =============================================
#           RESULTADO FINAL
# =============================================
def mostrar_resultado_final(tablero, puntaje, disparos_restantes, estado):
    print("\n" + "=" * 50)
    print("JUEGO FINALIZADO")
    print("=" * 50)

    if estado == EstadoJuego.GANADO:
        titulo = "MAESTRO" if puntaje >= 100 else "CAMPEÓN"
        print(f"\n ¡FELICITACIONES, {titulo}! 🏆")
        print("¡Hundiste todos los barcos enemigos!")
        print("\n Tu desempeño:")
        tablero.mostrar_vista_jugador()

    elif estado == EstadoJuego.PERDIDO_SIN_DISPAROS:
        print("\n ¡PERDISTE! Te quedaste sin disparos.")
        print(" No lograste hundir todos los barcos.")
        print("\n Solución:")
        tablero.mostrar_tablero_original()
        print("\n Tus disparos:")
        tablero.mostrar_vista_jugador()

    elif estado == EstadoJuego.RENDIDO:
        print("\n JUEGO INTERRUMPIDO")
        print("Decidiste rendirte antes de terminar.")
        resp = input("\n¿Querés ver dónde estaban los barcos? (s/n): ").strip().lower()
        if resp in ["", "s", "si"]:
            print("\n Solución:")
            tablero.mostrar_tablero_original()
        print("\n Tus disparos:")
        tablero.mostrar_vista_jugador()

    disparos_usados = DISPAROS_TOTALES - disparos_restantes
    print(f"\n Puntaje final:        {puntaje} puntos")
    print(f" Disparos utilizados:  {disparos_usados} de 25")

    if estado == EstadoJuego.GANADO:
        print(" ¡Eres un estratega nato! 🎯")
    elif puntaje > 50:
        print(" ¡Buen intento! ¡La próxima es tuya!")
    else:
        print(" Consejo: ¡los barcos no se mueven! Estudiá patrones.")

    print("=" * 50 + "\n")

# =============================================
#           PROGRAMA PRINCIPAL
# =============================================
while True:
    mostrar_menu()
    opcion = leer_entero()

    if opcion == 1:
        jugar()
    elif opcion == 2:
        ranking.mostrar_top10()
    elif opcion == 3:
        db.cerrar_conexion()
        print("Gracias por jugar. ¡Hasta la próxima! 👋")
        break
    else:
        print("Opción inválida. Intentá nuevamente.")