def main():

    """
    Tienes una lista de productos, donde cada producto es un diccionario: [{"nombre": "Camisa", "precio": 50000}, {"nombre": "Pantalón", "precio": 80000}]:
•	Usa una dictionary comprehension para crear un nuevo diccionario donde los nombres de los productos sean las claves y los precios con un 19% de IVA incluido sean los valores.
Conceptos aplicados: Dictionary comprehensions, acceso a valores de diccionario.

    """
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]

    # Diccionario con precios + IVA (19%)
    productos_con_iva = {p["nombre"]: p["precio"] * 1.19 for p in productos}

    # Mostrar resultados
    print("Productos con IVA incluido:")
    for nombre, precio in productos_con_iva.items():
        print(f"{nombre}: ${precio:,.0f}")


if __name__ == "__main__":
    main()
