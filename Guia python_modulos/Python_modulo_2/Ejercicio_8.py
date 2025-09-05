def main():
    numeros = [-5, 10, -15, 20, -25, 30]

    # 1. Lista con solo los números positivos
    positivos = [n for n in numeros if n > 0]

    # 2. Lista con los cuadrados de todos los números
    cuadrados = [n**2 for n in numeros]

    # 3. Lista de strings "positivo" o "negativo" (ternario dentro de la comprensión)
    etiquetas = ["positivo" if n > 0 else "negativo" for n in numeros]

    # Mostrar resultados
    print(f"Lista original: {numeros}")
    print(f"Números positivos: {positivos}")
    print(f"Cuadrados de los números: {cuadrados}")
    print(f"Etiquetas positivo/negativo: {etiquetas}")


if __name__ == "__main__":
    main()
