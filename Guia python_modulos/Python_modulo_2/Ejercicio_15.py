import random

"""
Crea una versión del juego "Batalla Naval" en una cuadrícula de 5x5:
•	El programa debe "esconder" un barco de 3 casillas en una fila o columna aleatoria.
•	El jugador tiene 10 turnos para adivinar las coordenadas (ej. "A3") y hundir el barco.
•	El programa debe gestionar el tablero (una lista de listas), validar la entrada del usuario, indicar si un disparo fue "Agua" o "Tocado", y llevar la cuenta de los turnos.

•	Al final, debe declarar si el jugador ganó o perdió.
Conceptos integrados: Lógica de juegos, listas anidadas, funciones, bucles while y for, condicionales, random, manipulación de strings.

"""


# Crear tablero vacío
def crear_tablero():
    return [["~"] * 5 for _ in range(5)]


# Mostrar tablero con coordenadas
def mostrar_tablero(tablero):
    print("   1  2  3  4  5")
    filas = ["A", "B", "C", "D", "E"]
    for i, fila in enumerate(tablero):
        print(f"{filas[i]}  " + "  ".join(fila))


# Colocar un barco de 3 casillas en fila o columna
def colocar_barco():
    orientacion = random.choice(["H", "V"])  # Horizontal o Vertical
    fila = random.randint(0, 4)
    col = random.randint(0, 4)

    if orientacion == "H":
        while col > 2:  # evitar que se salga del tablero
            col = random.randint(0, 2)
        return [(fila, col), (fila, col + 1), (fila, col + 2)]
    else:  # Vertical
        while fila > 2:
            fila = random.randint(0, 2)
        return [(fila, col), (fila + 1, col), (fila + 2, col)]


# Convertir coordenadas tipo "A3" a índices (fila, col)
def convertir_coordenada(coordenada):
    filas = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
    try:
        fila = filas[coordenada[0].upper()]
        col = int(coordenada[1]) - 1
        if fila in range(5) and col in range(5):
            return (fila, col)
    except:
        return None
    return None


def main():
    tablero = crear_tablero()
    barco = colocar_barco()
    aciertos = []
    turnos = 10

    print("🚢 Bienvenido a Batalla Naval 🚢")
    print("Debes hundir el barco de 3 casillas en un tablero de 5x5.")
    print("Ejemplo de coordenada: A3")

    while turnos > 0:
        mostrar_tablero(tablero)
        print(f"\nTurnos restantes: {turnos}")
        jugada = input("Ingresa una coordenada (ej. A3): ").strip()

        pos = convertir_coordenada(jugada)
        if not pos:
            print("Coordenada inválida. Usa formato A1 - E5.")
            continue

        if pos in aciertos or tablero[pos[0]][pos[1]] in ["X", "O"]:
            print("Ya disparaste en esa posición.")
            continue

        if pos in barco:
            print("¡Tocado!")
            tablero[pos[0]][pos[1]] = "X"
            aciertos.append(pos)
            if len(aciertos) == 3:
                print("\n ¡Hundiste el barco! ¡Ganaste!")
                mostrar_tablero(tablero)
                break
        else:
            print(" Agua...")
            tablero[pos[0]][pos[1]] = "O"
            turnos -= 1
    else:
        print("\n Te quedaste sin turnos. ¡Perdiste!")
        print("El barco estaba en:")
        for f, c in barco:
            tablero[f][c] = "B"
        mostrar_tablero(tablero)


if __name__ == "__main__":
    main()
