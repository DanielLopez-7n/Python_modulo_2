def main():

    """
    Crea un programa que pida un número y, usando un operador ternario, asigne a una variable el texto "Par" o "Impar". Luego, imprime el resultado. Adicionalmente, si el número es múltiplo de 5, debe imprimir un mensaje extra.
    Conceptos aplicados: Operador ternario, operador módulo (%), if.

    """
    # Bucle infinito: "mientras sea verdadero" (se repite hasta encontrar un 'break')
    while True:
        # Pedir al usuario: si escribe "x" salimos; si presiona Enter seguimos.
        # .lower() convierte la respuesta a minúsculas para que "X" y "x" sean iguales.
        usuario = str(input("Para salir: X  Para seguir: [Enter] \n")).lower()
        
        # Si el usuario escribió 'x', rompemos el bucle y termina el programa
        if usuario == "x":
            break


        # Pedimos un número y lo convertimos a entero
        numero = int(input("Escribe un numero: "))

        # Operador ternario:
        # "Par" si numero % 2 == 0 (residuo 0 al dividir entre 2), sino "Impar"
        resultado = "Par" if numero % 2 == 0 else "Impar"

        # Mostramos si el número es par o impar (f-string para insertar variables)
        print(f"El numero {numero} es {resultado}")

        # Otro ternario: comprobamos si es múltiplo de 5 (numero % 5 == 0)
        # Asignamos el texto correspondiente y luego lo imprimimos
        multiplo = "Ademas es multiplo de 5" if numero % 5 == 0 else "No es multiplo de 5"
        print(multiplo)


# Punto de entrada: si este archivo se ejecuta directamente, llama a main()
if __name__ == "__main__":
    main()
