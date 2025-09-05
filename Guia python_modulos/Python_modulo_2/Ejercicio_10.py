def transpuesta_for(matriz):

    """
Crea una función que reciba una matriz (lista de listas) y devuelva su transpuesta. La transpuesta se logra intercambiando filas por columnas.
•	Ejemplo: [[1, 2, 3], [4, 5, 6]] se convierte en [[1, 4], [2, 5], [3, 6]].
•	Resuelve este problema usando bucles for anidados y luego intenta resolverlo con una list comprehension anidada.
Conceptos aplicados: Listas anidadas (matrices), bucles anidados, list comprehensions anidadas.


    """
    # Creamos una lista vacía para la transpuesta
    transpuesta = []

    # Recorremos columnas de la matriz original
    for i in range(len(matriz[0])):
        nueva_fila = []  # Cada columna se vuelve fila
        for j in range(len(matriz)):
            nueva_fila.append(matriz[j][i])
        transpuesta.append(nueva_fila)

    return transpuesta


def transpuesta_comprehension(matriz):
    # Misma lógica pero con list comprehension anidada
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]


def main():
    matriz = [[1, 2, 3], [4, 5, 6]]

    print("Matriz original:")
    print(matriz)

    print("\nTranspuesta con for anidado:")
    print(transpuesta_for(matriz))

    print("\nTranspuesta con list comprehension:")
    print(transpuesta_comprehension(matriz))


if __name__ == "__main__":
    main()
