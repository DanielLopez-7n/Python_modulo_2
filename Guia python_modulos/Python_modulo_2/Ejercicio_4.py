import random #Importar random para que la pc elija

def main():

    """Implementa el clásico juego para jugar contra la computadora.
•	El usuario elige una opción y la computadora elige una al azar.
•	El programa determina el ganador basándose en las reglas (piedra vence a tijeras, tijeras a papel, papel a piedra).
•	Se debe llevar un conteo de las victorias del jugador y de la computadora. El juego termina cuando uno de los dos llegue a 3 victorias.
    Conceptos aplicados: random.choice(), bucle while, if/elif/else, contadores, f-strings.
    """
    #Contador de victorias

    victorias_jugador = 0
    victorias_pc = 0

    #Opciones validas
    opciones = ["piedra", "papel", "tijera"]
    salir = ["salir"]

    #Mientras que nadie llegue a 3 victorias, el juego sigue
    while victorias_jugador < 3 and victorias_pc < 3:
        #Se pide opcion al jugador
        jugador = input("Escribe: PIEDRA, PAPEL o TIJERA \n SALIR (X) -> ").lower()

        #Salir
        if (jugador in salir):
            break
        #validar que el jugador escriba una opcion valida
        if jugador not in opciones:
            print("Opcion no valida")
            break

        #pc elige
        pc = random.choice(opciones)

        print(f"Elegiste {jugador}")
        print(f"La pc elijio {pc}")

        if jugador == pc:
            print("Empate")
        elif (jugador == "piedra" and pc == "tijera")\
            or (jugador == "papel" and pc == "piedra")\
            or (jugador == "tijera" and pc == "papel"):
            print("Ganaste esta ronda")
            victorias_jugador += 1
        else:
            print("PC ganó esta ronda")
            victorias_pc += 1

        #Mostrar contadores
        print(f"Marcador -> Tú {victorias_jugador} | PC {victorias_pc}")

    #Cuando alguien llega a las 3 victorias

    if victorias_jugador == 3:
        print("Ganasté!")
    else:
        print("Ganó la PC")

if __name__ == "__main__":
    main()
