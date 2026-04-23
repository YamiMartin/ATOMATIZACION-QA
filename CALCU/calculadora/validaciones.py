from .calculos_funciones import CalculatorError


def parsear_numero(texto: str) -> float:
    """
    Convierte texto a float aceptando coma o punto como decimal.
    Ejemplos válidos: '3,14' , '3.14'
    """
    t = texto.strip().replace(",", ".")
    try:
        return float(t)
    except ValueError:
        raise CalculatorError("Entrada inválida: debe ser un número (ej: 3.14 o 3,14).")


def validar_opcion(opcion_texto: str) -> int:
    """
    Valida que la opción sea 1..4.
    """
    try:
        opcion = int(opcion_texto.strip())
    except ValueError:
        raise CalculatorError("Opción inválida. Elegí 1, 2, 3 o 4.")

    if opcion not in (1, 2, 3, 4):
        raise CalculatorError("Opción inválida. Elegí 1, 2, 3 o 4.")

    return opcion