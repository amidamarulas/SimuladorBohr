# examples/example_usage.py
"""
Ejemplo de uso de la librería SimuladorBohr.
Muestra energías, radios, transiciones y genera gráficas.
"""

from SimuladorBohr.energy import energy_ev
from SimuladorBohr.radius import orbit_radius
from SimuladorBohr.transitions import transition_energy_ev, wavelength, frequency
from SimuladorBohr.plotting import plot_energy_levels, plot_orbits

def main():
    Z = 1  # hidrógeno
    print("=== Niveles de energía y radios ===")
    for n in range(1,5):
        print(f"n={n}: E = {energy_ev(n, Z):.3f} eV, r = {orbit_radius(n, Z):.2e} m")

    print("\n=== Transición 3 → 2 ===")
    dE = transition_energy_ev(3,2,Z)
    lam = wavelength(3,2,Z)
    nu = frequency(3,2,Z)
    print(f"ΔE = {dE:.3f} eV, λ = {lam*1e9:.2f} nm, ν = {nu:.2e} Hz")

    print("\n=== Graficando ===")
    plot_energy_levels(Z, max_n=6)
    plot_orbits(Z, ns=[1,2,3])

if __name__ == "__main__":
    main()
