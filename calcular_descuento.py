def calcular_descuento(precio, porcentaje_descuento):
    """
     Docstring obligatorio según PEP 8.
     Explica qué hace la función, qué recibe y qué retorna.

    Args:
        precio (float): Precio original del producto.
        porcentaje_descuento (float): Descuento expresado en porcentaje (0–100).

    Returns:
        float: Precio final después de aplicar el descuento.

    Raises:
        ValueError: Si los valores ingresados no son válidos.
    """

    #  Validación de datos: buena práctica de seguridad y estabilidad
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100.")

    #  Variable con nombre claro (no usar 'p' o 'd')
    descuento = precio * (porcentaje_descuento / 100)

    #  Espacios alrededor de operadores (recomendación PEP 8)
    precio_final = precio - descuento

    #  Siempre retornar una variable clara, no expresiones complejas directamente
    return precio_final


# ----- Pruebas rápidas -----
#  Bloque de pruebas con if __name__ == "__main__": (buena práctica recomendada)
if __name__ == "__main__":

    #  Ejemplos de ejecución clara para depuración o demostración
    print(calcular_descuento(10000, 20))  # Esperado: 8000
    print(calcular_descuento(50000, 15))  # Esperado: 42500
