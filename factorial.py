"""Módulo para calcular el factorial de un número."""

def factorial(n: int) -> int:
    """Calcula el factorial de un número entero no negativo."""
    if n < 0:
        raise ValueError("No definido para números negativos.")
    if n in (0, 1):
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado