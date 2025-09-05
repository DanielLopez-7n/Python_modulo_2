def main():
    """ Crea un programa que calcule el precio de una entrada de cine basándose en la edad del cliente y si es estudiante:
       Reglas:
       •	Niños (menores de 12 años): $10.000.
       •	Jóvenes (12 a 17 años): $15.000.
       •	Adultos (18 años en adelante): $20.000.
       •	Si el cliente es estudiante (independientemente de la edad), tiene un 10% de descuento.
       El programa debe pedir la edad y si es estudiante ('si' o 'no').
       Conceptos aplicados: if/elif/else anidados, operadores lógicos (and, or), input(), int(), lower(), f-strings.
       """
    # "Tipo de usuario"
    cliente = str(input("Tipo de cliente: (niño, adulto, joven): ")).lower()
    est = str(input("¿Es estudiante? (si/no): ")).lower()
    edad = int(input("Edad: "))
    print("\n")

    # Llamar a la función y obtener el precio base
    precio = Clientes(cliente, edad)

    # Si es estudiante, aplicar 10% de descuento
    if est == "si":
        print("Los estudiantes tienen descuento del 10%")
        precio = precio - (precio * 0.10)
    else:
        print("No hay descuento.")

    # Mostrar precio final
    if precio > 0:   # Verifica que sea válido
        print(f"El precio final de la entrada es: ${precio:,.0f}")


def Clientes(cliente, edad):
    """Retorna el precio según el tipo de cliente y la edad"""
    if cliente == "niño" and edad <= 12:
        return 10000
    elif cliente == "joven" and 12 <= edad <= 17:
        return 15000
    elif cliente == "adulto" and edad >= 18:
        return 20000
    else:
        print("Tipo de usuario no válido")
        return 0   # Devuelve 0 si no coincide con ningún caso


if __name__ == "__main__":
    main()
