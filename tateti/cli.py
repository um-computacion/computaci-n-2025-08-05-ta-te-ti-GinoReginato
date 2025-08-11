from tateti import Tateti, JuegoTerminadoException

def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()

    while True:
        print("\nTablero:")
        juego.tablero.mostrar()
        print(f"Turno de {juego.turno.nombre} ({juego.turno.ficha})")

        try:
            fil = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese col (0-2): "))
            juego.ocupar_una_de_las_casillas(fil, col)
        except JuegoTerminadoException as e:
            print(e)
            juego.tablero.mostrar()
            break
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
