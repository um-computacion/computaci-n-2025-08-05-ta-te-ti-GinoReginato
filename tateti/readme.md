# Tateti en Python
## Gino Reginato   
## Legajo: 63280
## Carrera: Informatica

Este proyecto implementa el clásico juego de **Tateti** (Tres en línea) para jugar en consola entre dos personas.

## Estructura del proyecto

- **`jugador.py`**: Define la clase `Jugador`, que almacena el nombre y la ficha de cada participante.
- **`tablero.py`**: Contiene la clase `Tablero`, que maneja la representación del tablero, las validaciones de posiciones y la lógica para detectar ganadores o empates.
- **`tateti.py`**: Implementa la clase `Tateti`, que coordina el juego, administra los turnos y detecta el fin de la partida.
- **`cli.py`**: Proporciona una interfaz de línea de comandos para jugar en modo interactivo.
- **`test_tateti.py`**: Conjunto de pruebas unitarias para verificar el correcto funcionamiento de la lógica del juego.

## Cómo ejecutar el juego

1. Clonar o descargar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python cli.py
