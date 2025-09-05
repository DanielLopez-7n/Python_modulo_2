def generar_diccionario(nombres, notas):
    """
    Dadas dos listas, una con nombres de estudiantes y otra con sus respectivas notas finales, crea una función que las combine para generar un diccionario. Las claves serán los nombres y los valores las notas:
    Luego, itera sobre el diccionario resultante para imprimir un reporte del tipo: "El estudiante [Nombre] tiene una nota de [Nota]".
    Conceptos aplicados: Funciones, zip(), dict(), bucle for sobre diccionarios.

    Recibe dos listas: nombres y notas.
    Retorna un diccionario con el formato {nombre: nota}.
    """
    return dict(zip(nombres, notas))


def main():
    # Dos listas iniciales: estudiantes y sus notas
    estudiantes = ["Ana", "Luis", "María", "Carlos"]
    notas = [4.5, 3.8, 5.0, 4.2]

    # Generamos el diccionario uniendo los nombres con sus notas
    reporte = generar_diccionario(estudiantes, notas)

    # Recorremos el diccionario y mostramos el reporte
    for nombre, nota in reporte.items():
        print(f"El estudiante {nombre} tiene una nota de {nota}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
