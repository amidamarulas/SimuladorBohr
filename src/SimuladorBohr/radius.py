"""
SimuladorBohr - radius.py
-----------------

Este módulo contiene funciones para calcular los radios de las órbitas
electrónicas en el modelo atómico de Bohr.

Se utilizan las constantes definidas en constants.py.
"""

from .constants import a0


"""
La fórmula del radio de la órbita en el modelo de Bohr es:

    r_n = a0 * (n^2 / Z)

donde:
- a0 : radio de Bohr fundamental (≈ 5.29 × 10⁻¹¹ m)
- n  : número cuántico principal (1, 2, 3, ...)
- Z  : número atómico

Este radio corresponde a la distancia más probable entre el electrón
y el núcleo en el modelo de Bohr. Para hidrógeno (Z=1, n=1) se obtiene a0.
"""


def radius(n: int, Z: int = 1) -> float:
    """
    Calcula el radio de la órbita n para un átomo con número atómico Z.

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

    return a0 * (n**2 / Z)


def summary(Z: int = 1, max_n: int = 5):
    """
    Genera un resumen con los radios de las primeras órbitas.

    Parámetros
    ----------
    Z : int
        Número atómico.
    max_n : int
        Nivel máximo a calcular.

    Retorna
    -------
    dict
        Diccionario con {n: r_n}.
    """
    data = {}
    for n in range(1, max_n + 1):
        data[n] = radius(n, Z)
    return data


if __name__ == "__main__":
    """
    Si se ejecuta este archivo directamente,
    se imprimen los radios de las primeras órbitas
    del hidrógeno (Z=1).
    """
    for n, r in summary(Z=1, max_n=5).items():
        print(f"n={n}: r = {r:.3e} m")