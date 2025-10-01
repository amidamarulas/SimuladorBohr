"""
SimuladorBohr - energy.py
-----------------

Este módulo contiene funciones para calcular las energías de los niveles
electrónicos en el modelo atómico de Bohr.
"""

from .constants import H, E_CHARGE, M_E, EPSILON_0

# ===============================
# Funciones de energía
# ===============================
def energy_joule(n: int, Z: int = 1) -> float:
    """
    Calcula la energía del nivel n en julios (J).

    Parámetros
    ----------
    n : int
        Número cuántico principal (n >= 1).
    Z : int, opcional
        Número atómico (carga nuclear). Por defecto 1 (hidrógeno).

    Retorna
    -------
    float
        Energía del nivel n en julios (valor negativo).

    Fórmula de Bohr:
    E_n = - (M_E * e^4 * Z^2) / (8 * ε0^2 * h^2 * n^2)
    """
    if n < 1:
        raise ValueError("El número cuántico principal n debe ser >= 1.")

    E = - (M_E * E_CHARGE**4 * Z**2) / (8 * EPSILON_0**2 * H**2 * n**2)
    return E


def energy_ev(n: int, Z: int = 1) -> float:
    """
    Calcula la energía del nivel n en electronvoltios (eV).
    """
    return energy_joule(n, Z) / E_CHARGE

# ===============================
# Utilidad
# ===============================
def summary(Z: int = 1, max_n: int = 5):
    """
    Genera un resumen con las energías de los primeros niveles.
    """
    data = {}
    for n in range(1, max_n + 1):
        data[n] = (energy_joule(n, Z), energy_ev(n, Z))
    return data


if __name__ == "__main__":
    # Ejemplo: imprimir energías para hidrógeno (Z=1)
    for n, (EJ, EV) in summary(Z=1, max_n=5).items():
        print(f"n={n}: {EJ:.3e} J  |  {EV:.3f} eV")

