"""
    Crea una función que reciba una frase y una letra. La función debe devolver una lista con todos los índices (posiciones) en los que aparece esa letra en la frase.
    Ejemplo: encontrar_indices("Hola SENA", "a") debería devolver [3, 8].
    Conceptos aplicados: Funciones, enumerate(), bucle for, list.append().

    Args:
        frase: str, para guardar la frase
        letra: str guardar letra a buscar en futuro
"""


def encontrar_indices(frase, letra):
    indices = []  # Lista vacía para guardar las posiciones

    for i, caracter in enumerate(frase):  # Recorremos la frase letra por letra
        if caracter.lower() == letra.lower():  # Comparar sin importar mayúsculas/minúsculas
            indices.append(i)  # Guardar la posición en la lista

    return indices


def main():
    # Pedir al usuario la frase y la letra
    frase = input("Escribe una frase: ")
    letra = input("Escribe la letra a buscar: ")

    # Usamos la función encontrar_indices
    resultado = encontrar_indices(frase, letra)

    # Mostramos el resultado
    if resultado:  # Si la lista no está vacía
        print(f"La letra '{letra}' aparece en las posiciones: {resultado}")
    else:
        print(f"La letra '{letra}' no aparece en la frase.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
