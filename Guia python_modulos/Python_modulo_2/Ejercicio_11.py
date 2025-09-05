def validar_cedula(cedula):

    """
    Escribe una función que valide un número de cédula (como string) basado en una regla simple: la suma de sus dígitos debe ser un número par. La función debe devolver True si es válido y False si no:
•	Adicionalmente, el programa principal debe pedir al usuario su cédula hasta que ingrese una válida, usando un bucle.
Conceptos aplicados: Funciones, bucle while, conversión de tipos (str a int), bucle for sobre un string.

    """
    # Sumar cada dígito de la cédula
    suma = 0
    for digito in cedula:
        suma += int(digito)  # Convertimos cada caracter a número y lo sumamos

    # La cédula es válida si la suma es un número par
    return suma % 2 == 0


def main():
    while True:
        cedula = input("Ingrese su número de cédula: ")

        # Validar que la entrada contenga solo dígitos
        if not cedula.isdigit():
            print("⚠️ La cédula debe contener solo números.")
            continue

        # Verificamos si es válida
        if validar_cedula(cedula):
            print("Cédula válida")
            break
        else:
            print("Cédula inválida, la suma de los dígitos no es par. Intente de nuevo.")


if __name__ == "__main__":
    main()
