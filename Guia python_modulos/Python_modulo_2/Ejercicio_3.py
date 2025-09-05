def main():

    """Escribe un programa que pida al usuario crear una contraseña y la valide usando un bucle while. El bucle solo terminará cuando la contraseña cumpla todos los criterios:
•	Mínimo 8 caracteres de longitud.
•	Contiene al menos una letra mayúscula.
•	Contiene al menos un número.
•	En cada intento fallido, el programa debe indicar qué regla no se cumplió.
    Conceptos aplicados: Bucle while True, if/elif/else, len(), métodos de string (isupper(), islower(), isdigit()), break.
    """
    print("Creador de contraseñas: mínimo 8 caracteres, al menos 1 MAYÚSCULA y 1 número.\n")

    while True:  # Mientras sea verdadero (bucle infinito hasta que rompamos con break)
        contrasena = input("Crea una contraseña: ")

        # Lista para acumular las reglas que NO se cumplan
        errores = []

        # Regla 1: longitud mínima
        if len(contrasena) < 8:
            errores.append("• Debe tener al menos 8 caracteres.")

        # Regla 2: al menos una letra MAYÚSCULA
        tiene_mayuscula = any(c.isupper() for c in contrasena)
        if not tiene_mayuscula:
            errores.append("• Debe incluir al menos una letra MAYÚSCULA (A–Z).")

        # Regla 3: al menos un número
        tiene_numero = any(c.isdigit() for c in contrasena)
        if not tiene_numero:
            errores.append("• Debe incluir al menos un número (0–9).")

        # ¿Se cumplieron todas las reglas?
        if not errores:
            print("Contraseña válida. ¡Guardada!")
            break  # Romper/salir del bucle while
        else:
            print("La contraseña no cumple las siguientes reglas:")
            for falta in errores:
                print(falta)
            print("Inténtalo de nuevo.\n")


if __name__ == "__main__":
    main()
