# src/SimuladorBohr/radius.py

"""
Módulo: radius
Cálculo del radio de las órbitas electrónicas en el modelo de Bohr.

Este módulo utiliza las constantes físicas definidas en `constants.py` 
para calcular el radio de Bohr y el radio de la órbita correspondiente 
a un número cuántico principal n.
"""

from . import constants as c


def bohr_radius() -> float:
    """
    Devuelve el radio de Bohr (a₀) en metros.
    """
    return (c.HBAR**2) / (c.M_E * c.E_CHARGE**2 / (4 * c.PI * c.EPSILON_0))


def orbit_radius(n: int) -> float:
    """
    Calcula el radio de la órbita para un nivel cuántico principal n
    en el átomo de hidrógeno (modelo de Bohr).

    Parámetros:
    ----------
    n : int
        Número cuántico principal (n >= 1).

    Retorna:
    -------
    float
        Radio de la órbita en metros.
    """
    if n < 1:
        raise ValueError("El número cuántico principal n debe ser mayor o igual a 1.")
    return n**2 * bohr_radius()


# Ejemplo de uso interno (se puede borrar o dejar como test rápido)
if __name__ == "__main__":
    print("Radio de Bohr (a0):", bohr_radius(), "m")
    for n in range(1, 4):
        print(f"Radio de la órbita n={n}: {orbit_radius(n)} m")
