def main():

    """
    Diseña un pequeño juego de aventura basado en texto. El jugador comienza en una habitación y puede tomar decisiones ('ir al norte', 'abrir cofre'):
•	El juego debe tener al menos 3 habitaciones y un estado final (ganar o perder).
•	Utiliza un bucle while para el bucle principal del juego y estructuras if/elif/else para manejar las decisiones del jugador y el estado del juego.
Conceptos integrados: Bucles, condicionales, manejo de estado con variables, input().

    """
    print("Bienvenido al juego de aventura")
    print("Estás en una mazmorra misteriosa...")

    # Estado del juego
    habitacion = "entrada"
    juego_activo = True

    while juego_activo:
        if habitacion == "entrada":
            print("\nTe encuentras en la entrada de la mazmorra.")
            print("Opciones: 'norte' para avanzar, 'salir' para rendirte.")
            decision = input("¿Qué haces?: ").lower()

            if decision == "norte":
                habitacion = "pasillo"
            elif decision == "salir":
                print("Has abandonado la aventura.")
                juego_activo = False
            else:
                print("No entiendo esa acción...")

        elif habitacion == "pasillo":
            print("\nCaminas por un pasillo oscuro.")
            print("Opciones: 'izquierda' (huele a comida), 'derecha' (ves un cofre).")
            decision = input("¿Qué haces?: ").lower()

            if decision == "izquierda":
                habitacion = "cocina"
            elif decision == "derecha":
                habitacion = "tesoro"
            else:
                print("Esa acción no es válida.")

        elif habitacion == "cocina":
            print("\nEntraste en la cocina...")
            print("¡Oh no! Un ogro te atrapó. 💀 Game Over.")
            juego_activo = False

        elif habitacion == "tesoro":
            print("\n¡Encontraste un cofre de tesoro brillante! 🎉")
            print("¡Has ganado la aventura! 🏆")
            juego_activo = False


if __name__ == "__main__":
    main()
