import random

def main():

    """
    •	Crea un programa que simule el lanzamiento de dos dados 10,000 veces.
•	Usa un diccionario para contar la frecuencia de cada posible suma de los dados (de 2 a 12).
•	Al final, imprime un reporte con la frecuencia de cada suma.
Conceptos aplicados: random.randint(), bucles, diccionarios como contadores, método get().

    """
    # Diccionario vacío para guardar las frecuencias
    frecuencias = {}

    # Lanzamos los dados 10,000 veces
    for _ in range(10000):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2

        # Usamos .get() para incrementar el contador
        frecuencias[suma] = frecuencias.get(suma, 0) + 1

    # Reporte final
    print("Frecuencia de las sumas en 10,000 lanzamientos:\n")
    for suma in range(2, 13):  # de 2 a 12
        print(f"Suma {suma}: {frecuencias.get(suma, 0)} veces")


if __name__ == "__main__":
    main()
