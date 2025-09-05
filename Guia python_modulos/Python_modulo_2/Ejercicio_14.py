import random

def mostrar_tablero(palabra_secreta, letras_adivinadas, vidas):
    tablero = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
    print("\nPalabra: " + " ".join(tablero))
    print(f"Letras intentadas: {', '.join(sorted(letras_adivinadas))}")
    print(f"Vidas restantes: {vidas}")

    """
    Diseña una versión para consola del clásico juego del "Ahorcado". El programa debe ser capaz de gestionar toda la lógica del juego, desde la selección de la palabra hasta determinar si el jugador ha ganado o perdido.
Lógica del Juego:
•	El programa debe tener una lista predefinida de palabras secretas y seleccionar una al azar para cada partida.
•	Debe mostrar al jugador el "tablero", que consiste en guiones bajos representando las letras de la palabra secreta y una lista de las letras ya intentadas.
•	El jugador tiene un número limitado de intentos (ej. 6 vidas).
•	En cada turno, el jugador ingresa una letra. El programa debe validar si la entrada es una sola letra y si no ha sido intentada antes.
•	Si la letra está en la palabra secreta, se revelan todas sus apariciones (ej. _ _ _ _ _ -> _ a _ a _). Si no está, el jugador pierde una vida.
•	El juego termina cuando el jugador adivina todas las letras (gana) o se queda sin vidas (pierde).
Conceptos integrados: Lógica de juegos, random.choice, listas y/o sets (para letras adivinadas), manipulación de strings, bucles while, condicionales if/else, funciones para modularizar (ej. mostrar_tablero(), validar_entrada()), manejo de estado del juego.

    """


def validar_entrada(letra, letras_adivinadas):
    if len(letra) != 1 or not letra.isalpha():
        print("⚠️ Debes ingresar una sola letra.")
        return False
    if letra in letras_adivinadas:
        print("⚠️ Ya intentaste esa letra.")
        return False
    return True


def main():
    palabras = ["python", "programacion", "ahorcado", "computador", "juego"]
    palabra_secreta = random.choice(palabras)

    vidas = 6
    letras_adivinadas = set()

    print("🎮 Bienvenido al juego del Ahorcado 🎮")

    while vidas > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas, vidas)

        letra = input("Ingresa una letra: ").lower()

        if not validar_entrada(letra, letras_adivinadas):
            continue

        letras_adivinadas.add(letra)

        if letra in palabra_secreta:
            print(f"✅ ¡Bien! La letra '{letra}' está en la palabra.")
            # Revisar si ya se adivinó toda la palabra
            if all(l in letras_adivinadas for l in palabra_secreta):
                print(f"\n🎉 ¡Ganaste! La palabra era: {palabra_secreta}")
                break
        else:
            vidas -= 1
            print(f"❌ La letra '{letra}' no está en la palabra.")

    else:
        print(f"\n💀 Te quedaste sin vidas. La palabra era: {palabra_secreta}")


if __name__ == "__main__":
    main()
