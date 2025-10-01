"""
SimuladorBohr - radius.py
-----------------

Este módulo contiene funciones para calcular los radios de las órbitas
electrónicas en el modelo atómico de Bohr.
"""

from .constants import A_0

def radius(n: int, Z: int = 1) -> float:
    """
    Calcula el radio de la órbita n para un átomo con número atómico Z.

    Fórmula:
        r_n = A_0 * (n^2 / Z)

    Parámetros
    ----------
    n : int
        Número cuántico principal (n >= 1).
    Z : int, opcional
        Número atómico. Por defecto 1 (hidrógeno).

    Retorna
    -------
    float
        Radio de la órbita en metros.
    """
    if n < 1:
        raise ValueError("El número cuántico principal n debe ser >= 1.")

    return A_0 * (n**2 / Z)

def summary(Z: int = 1, max_n: int = 5):
    """Genera un diccionario con los radios de las primeras órbitas."""
    data = {}
    for n in range(1, max_n + 1):
        data[n] = radius(n, Z)
    return data

if __name__ == "__main__":
    for n, r in summary(Z=1, max_n=5).items():
        print(f"n={n}: r = {r:.3e} m")
