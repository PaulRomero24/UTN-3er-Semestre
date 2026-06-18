
class Coordenadas:
    # Constructor privado — equivalente al throw de Java
    def __init__(self):
        raise Exception("Clase de utilidad: no se puede instanciar")

    @staticmethod
    def letra_a_columna(letra: str) -> int:
        columnas = {
            'A': 0, 'B': 1, 'C': 2, 'D': 3,
            'E': 4, 'F': 5, 'G': 6, 'H': 7
        }
        return columnas.get(letra, -1)  # -1 si la letra no existe

    @staticmethod
    def parsear_coordenada(coordenada: str):
        """
        Convierte una coordenada (ej: 'A5', 'h3') a [fila, columna].
        Devuelve None si es inválida.
        """
        if not coordenada or len(coordenada) < 2:
            return None

        # Normalizar: mayúsculas y sin espacios — equivalente a trim().toUpperCase()
        coordenada = coordenada.strip().upper()

        letra = coordenada[0]
        num_str = coordenada[1:].strip()

        # Validar que el resto sea numérico — equivalente a matches("\\d+")
        if not num_str.isdigit():
            return None

        columna = Coordenadas.letra_a_columna(letra)

        try:
            fila = int(num_str) - 1  # -1 porque el jugador ve 1-8 pero el tablero es 0-7
        except ValueError:
            return None

        # Validar que esté dentro del tablero
        if columna < 0 or columna > 7 or fila < 0 or fila > 7:
            return None

        return [fila, columna]  # equivalente a new int[]{fila, columna}