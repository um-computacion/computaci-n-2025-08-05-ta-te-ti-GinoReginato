from tablero import Tablero, PosOcupadaException
from jugador import Jugador

class JuegoTerminadoException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class Tateti:
    def __init__(self, nombre_j1=None, nombre_j2=None):
        self.tablero = Tablero()
        # Si no se pasan nombres, los pedimos por input (modo interactivo)
        if nombre_j1 is None:
            nombre_j1 = input("Nombre jugador X: ")
        if nombre_j2 is None:
            nombre_j2 = input("Nombre jugador O: ")

        self.jugadores = [
            Jugador(nombre_j1, "X"),
            Jugador(nombre_j2, "O"),
        ]
        self.turno_idx = 0

    @property
    def turno(self):
        return self.jugadores[self.turno_idx]

    def ocupar_una_de_las_casillas(self, fil, col):
        if fil not in range(3) or col not in range(3):
            raise ValueError("Fila y columna deben ser 0, 1 o 2")
        
        self.tablero.poner_la_ficha(fil, col, self.turno.ficha)

        if self.tablero.hay_ganador():
            raise JuegoTerminadoException(f"Ganó {self.turno.nombre} ({self.turno.ficha})!")
        if self.tablero.esta_lleno():
            raise JuegoTerminadoException("Empate!")

        self.turno_idx = 1 - self.turno_idx
