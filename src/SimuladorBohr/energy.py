"""
MBohr - energy.py
-----------------

Este módulo contiene funciones para calcular las energías de los niveles
electrónicos en el modelo atómico de Bohr.
"""

from .constants import h, e, m_e, epsilon0
'''
 ===============================
 Funciones de energía
 ===============================
'''
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

        basado en:
        Fórmula de Bohr:
        E_n = - (m_e * e^4 * Z^2) / (8 * ε0^2 * h^2 * n^2)
    """
    if n < 1:
        raise ValueError("El número cuántico principal n debe ser >= 1.")

    E = - (m_e * e**4 * Z**2) / (8 * epsilon0**2 * h**2 * n**2)
    return E


def energy_ev(n: int, Z: int = 1) -> float:
    """
    Calcula la energía del nivel n en electronvoltios (eV).

    Parámetros
    ----------
    n : int
        Número cuántico principal (n >= 1).
    Z : int, opcional
        Número atómico. Por defecto 1 (hidrógeno).

    Retorna
    -------
    float
        Energía del nivel n en eV (valor negativo).
    """
    return energy_joule(n, Z) / e

'''
 ===============================
 Utilidad
 ===============================
'''
def summary(Z: int = 1, max_n: int = 5):
    """
    Genera un resumen con las energías de los primeros niveles.

    Parámetros
    ----------
    Z : int
        Número atómico.
    max_n : int
        Nivel máximo a calcular.

    Retorna
    -------
    dict
        Diccionario con {n: (E_J, E_eV)}.
    """
    data = {}
    for n in range(1, max_n + 1):
        data[n] = (energy_joule(n, Z), energy_ev(n, Z))
    return data


if __name__ == "__main__":
    # Ejemplo: imprimir energías para hidrógeno (Z=1)
    for n, (EJ, EV) in summary(Z=1, max_n=5).items():
        print(f"n={n}: {EJ:.3e} J  |  {EV:.3f} eV")
