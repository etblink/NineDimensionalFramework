import numpy as np
from scipy.special import spherical_jn

def wave_function_9d(x1, x2, x3, nu, alpha, rho, p1, p2, omega):
    """Compute the 9D wave function value at given coordinates"""
    # Spatial part
    r = np.sqrt(x1**2 + x2**2 + x3**2)
    spatial = spherical_jn(0, r)

    # Time-frequency part
    time_part = np.exp(1j * nu * omega)

    # Scaling part
    scale = np.exp(-alpha * r)

    # Resonance
    res = np.cos(rho * r)

    # Polarity
    pol = np.sin(p1 - p2)

    return spatial * time_part * scale * res * pol

def project_to_4d(grid_points=50):
    """Project 9D wave function to 4D spacetime"""
    x = np.linspace(-5, 5, grid_points)
    y = np.linspace(-5, 5, grid_points)
    z = np.linspace(-5, 5, grid_points)
    t = np.linspace(0, 2*np.pi, grid_points)

    X, Y, Z, T = np.meshgrid(x, y, z, t, indexing='ij')

    # Default parameters for higher dimensions
    nu = 1.0
    alpha = 0.5
    rho = 1.0
    p1 = 0.0
    p2 = np.pi/2
    omega = 1.0

    psi_4d = wave_function_9d(X, Y, Z, nu, alpha, rho, p1, p2, omega)
    return np.abs(psi_4d)

def compute_em_fields(psi_4d):
    """Compute electromagnetic fields from 4D wave function"""
    # Take gradients for E and B fields
    Ex, Ey, Ez = np.gradient(np.real(psi_4d))
    Bx, By, Bz = np.gradient(np.imag(psi_4d))

    return (Ex, Ey, Ez), (Bx, By, Bz)