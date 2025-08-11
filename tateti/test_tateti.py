import unittest
from tateti import Tateti, JuegoTerminadoException
from tablero import PosOcupadaException

class TestTateti(unittest.TestCase):

    def setUp(self):
        self.juego = Tateti(nombre_j1="Jugador1", nombre_j2="Jugador2")

    def test_movimiento_y_turno(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.tablero.contenedor[0][0], "X")
        self.assertEqual(self.juego.turno.ficha, "O")

    def test_posicion_ocupada(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        with self.assertRaises(PosOcupadaException):
            self.juego.ocupar_una_de_las_casillas(0, 0)

    def test_ganador_en_fila(self):
        self.juego.tablero.contenedor = [
            ["X", "X", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self.juego.turno_idx = 0
        with self.assertRaises(JuegoTerminadoException):
            self.juego.ocupar_una_de_las_casillas(0, 2)

if __name__ == "__main__":
    unittest.main()
