# 🚢 Batalla Naval — Python + PostgreSQL

Juego de Batalla Naval en consola con login de usuario y ranking persistente en PostgreSQL.

## Requisitos

- Python 3.10+
- PostgreSQL instalado y corriendo

## Instalación

### 1. Clonar el repositorio
```bash
git clone <url-del-repo>
cd batalla_naval
```

### 2. Crear y activar el entorno virtual
```bash
py -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Crear la base de datos en pgAdmin
- Abrí pgAdmin
- Ejecutá el archivo `schema.sql` en el Query Tool

### 5. Configurar la conexión en `main.py`
```python
db = Conexion(
    host="localhost",
    port=5432,
    database="batalla_naval",
    user="postgres",
    password="TU_CONTRASEÑA"  # <- Contraseña de tu pgAdmin
)
```

### 6. Correr el juego
```bash
python main.py
```

## Estructura del proyecto

```
batalla_naval/
├── Conexion.py       # Conexión a PostgreSQL
├── Login.py          # Login y registro de usuarios
├── Jugador.py        # Modelo del jugador
├── JugadorDao.py     # Operaciones de jugadores en BD
├── Ranking.py        # Muestra el Top 10
├── RankingDao.py     # Operaciones de ranking en BD
├── tablero.py        # Lógica del tablero
├── TipoBarco.py      # Tipos de barcos (enum)
├── Coordenadas.py     # Parseo de coordenadas
├── main.py           # Programa principal
├── schema.sql        # Estructura de la base de datos
├── requirements.txt  # Dependencias
└── README.md
```

## Cómo se juega

1. Registrate o iniciá sesión
2. Ingresá coordenadas como `A5`, `C3`, `H8`
3. Tenés **25 disparos** para hundir todos los barcos
4. Cada fallo resta **5 puntos** del puntaje inicial de **125**
5. Cada 5 disparos podés rendirte escribiendo `salir`

## Símbolos del tablero

| Símbolo | Significado |
|---------|-------------|
| `?` | Celda sin disparar |
| `O` | Agua |
| `X` | Impacto |
| `#` | Barco hundido |