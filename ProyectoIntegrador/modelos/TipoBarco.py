from enum import Enum

class TipoBarco(Enum):
    # CONSTANTES CON 2 VALORES (tamaño, símbolo) — equivalente al enum de Java
    SUBMARINO  = (1, 'S')
    DESTRUCTOR = (2, 'D')
    CRUCERO    = (3, 'C')
    

    # Constructor equivalente al TipoBarco(int tamaño, char simbolo) de Java
    def __init__(self, tamaño, simbolo):
        self.tamaño  = tamaño
        self.simbolo = simbolo

    # GETTERS
    def get_tamaño(self):
        return self.tamaño

    def get_simbolo(self):
        return self.simbolo

    # MÉTODO ESTÁTICO — equivalente a fromId() de Java
    @staticmethod
    def from_id(id):
        opciones = {
            1: TipoBarco.SUBMARINO,
            2: TipoBarco.DESTRUCTOR,
            3: TipoBarco.CRUCERO
        }
        if id not in opciones:
            raise ValueError(f"ID de barco no válido: {id}")
        return opciones[id]

    # MÉTODO DE INSTANCIA — equivalente a toId() de Java
    def to_id(self):
        ids = {
            TipoBarco.SUBMARINO:  1,
            TipoBarco.DESTRUCTOR: 2,
            TipoBarco.CRUCERO:    3
        }
        return ids[self]