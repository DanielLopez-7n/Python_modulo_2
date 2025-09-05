def main():
    """Desarrolla un programa que simule un menú de consola usando la estructura match-case. El programa mostrará una lista de comandos disponibles ("guardar", "cargar", "salir") y el usuario ingresará uno
•	El programa debe ejecutar una acción simulada para cada comando (ej. imprimir "Guardando archivo...").
•	Si el comando no es válido, debe mostrar un mensaje de error.
•	El programa debe seguir pidiendo comandos hasta que el usuario escriba "salir".
•	Conceptos aplicados: Bucle while, match-case, input(), lower().
    """
    while True:

        print("\n ---Menú de consola---")
        comando = input("Escribe la opción: (GUARDAR | CARGAR | SALIR) -> ").lower() #Pedir datos
#Casos
        match comando:
            case "guardar":
                print("Guardando archivo")
            case "cargar":
                print("Cargando archivo")
            case "salir":
                print("Saliendo del programa")
                break
            case _:
                print("Opción no valida")
                break


if __name__ == "__main__":
    main()
