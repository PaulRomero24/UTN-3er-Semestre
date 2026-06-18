import random



class Tablero:
    # CONSTANTES DEL TABLERO
    FILAS = 8
    COLUMNAS = 8

    def __init__(self):
        # Matrices equivalentes a los arrays bidimensionales de Java
        self.barcos = [[0] * self.COLUMNAS for _ in range(self.FILAS)]
        self.vista_jugador = [['?'] * self.COLUMNAS for _ in range(self.FILAS)]
        self.copia_original = [[0] * self.COLUMNAS for _ in range(self.FILAS)]
        self.__inicializar()

    # CREACION DEL TABLERO
    def __inicializar(self):
        for i in range(self.FILAS):
            for j in range(self.COLUMNAS):
                self.barcos[i][j] = 0
                self.vista_jugador[i][j] = '?'

    # AÑADIMOS LOS BARCOS
    def colocar_barco(self):
        from modelos.TipoBarco import TipoBarco
        self.__colocar(TipoBarco.SUBMARINO)
        self.__colocar(TipoBarco.CRUCERO)
        self.__colocar(TipoBarco.DESTRUCTOR)
        self.__colocar(TipoBarco.SUBMARINO)
        self.__colocar(TipoBarco.DESTRUCTOR)
        self.__copiar_barcos()

    def __colocar(self, tipo):
        from modelos.TipoBarco import TipoBarco
        tamaño = tipo.get_tamaño()
        id_barco = tipo.to_id()
        colocado = False

        while not colocado:
            fila = random.randint(0, self.FILAS - 1)
            columna = random.randint(0, self.COLUMNAS - 1)
            horizontal = random.choice([True, False])

            if horizontal and columna + tamaño <= self.COLUMNAS:
                # Verificar si las celdas están libres
                libre = all(self.barcos[fila][columna + j] == 0 for j in range(tamaño))
                if libre:
                    for j in range(tamaño):
                        self.barcos[fila][columna + j] = id_barco
                    colocado = True

            elif not horizontal and fila + tamaño <= self.FILAS:
                libre = all(self.barcos[fila + i][columna] == 0 for i in range(tamaño))
                if libre:
                    for i in range(tamaño):
                        self.barcos[fila + i][columna] = id_barco
                    colocado = True

    # COPIA DE SEGURIDAD DEL TABLERO
    def __copiar_barcos(self):
        for i in range(self.FILAS):
            self.copia_original[i] = self.barcos[i][:]  # equivalente a arraycopy de Java

    # SISTEMA DE DISPAROS
    def disparar(self, fila, columna):
        # Verificar límites
        if fila < 0 or fila >= self.FILAS or columna < 0 or columna >= self.COLUMNAS:
            return False
        # Verificar si ya se disparó ahí
        if self.vista_jugador[fila][columna] != '?':
            return False

        valor = self.barcos[fila][columna]
        if valor == 0:
            self.vista_jugador[fila][columna] = 'O'   # Agua
        else:
            self.vista_jugador[fila][columna] = 'X'   # Impacto
            self.barcos[fila][columna] = 0             # ✅ marca como golpeado
            if self.__barco_hundido(valor):
                self.__marcar_hundido(valor)
        return True

    def __barco_hundido(self, tipo):
        for i in range(self.FILAS):
            for j in range(self.COLUMNAS):
                if self.barcos[i][j] == tipo and self.vista_jugador[i][j] == '?':
                    return False   # aún hay partes sin tocar
        return True

    def __marcar_hundido(self, tipo):
        for i in range(self.FILAS):
            for j in range(self.COLUMNAS):
                if self.vista_jugador[i][j] == 'X':
                    self.vista_jugador[i][j] = '#'

    # VERIFICAR SI EL JUEGO TERMINÓ
    def juego_finalizado(self):
        for i in range(self.FILAS):
            for j in range(self.COLUMNAS):
                if self.barcos[i][j] > 0:
                    return False   # aún hay barcos
        return True

    # MOSTRAR TABLERO AL JUGADOR
    def mostrar_vista_jugador(self):
        print("    A B C D E F G H")
        for i in range(self.FILAS):
            print(f"{i + 1}  ", end="")
            for j in range(self.COLUMNAS):
                print(self.vista_jugador[i][j] + " ", end="")
            print()

    # MOSTRAR TABLERO CON UBICACIÓN DE BARCOS
    def mostrar_tablero_original(self):
        simbolos = {1: 'S', 2: 'D', 3: 'C'}
        print("\n=== UBICACIÓN DE LAS NAVES EN EL TABLERO ===")
        print("    A B C D E F G H")
        for i in range(self.FILAS):
            print(f"{i + 1}  ", end="")
            for j in range(self.COLUMNAS):
                id_barco = self.copia_original[i][j]
                simbolo = simbolos.get(id_barco, '~')
                print(simbolo + " ", end="")
            print()
        print("\nS = Submarino, C = Crucero, D = Destructor, ~ = Agua\n")

    # GETTERS
    def get_vista_jugador(self):
        return self.vista_jugador

    def get_copia_original(self):
        return self.copia_original