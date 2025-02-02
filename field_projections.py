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
    # Average over time dimension to get 3D fields
    psi_3d = np.mean(psi_4d, axis=-1)

    # Calculate gradients for real and imaginary parts
    grad_real = np.gradient(np.real(psi_3d))
    grad_imag = np.gradient(np.imag(psi_3d))

    # Extract E and B field components
    Ex, Ey, Ez = grad_real
    Bx, By, Bz = grad_imag

    # Normalize field strengths
    E_norm = np.sqrt(Ex**2 + Ey**2 + Ez**2)
    B_norm = np.sqrt(Bx**2 + By**2 + Bz**2)

    Ex, Ey, Ez = [E/E_norm.max() for E in (Ex, Ey, Ez)]
    Bx, By, Bz = [B/B_norm.max() for B in (Bx, By, Bz)]

    return (Ex, Ey, Ez), (Bx, By, Bz)