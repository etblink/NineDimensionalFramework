import numpy as np
from scipy.spatial.transform import Rotation

def generate_hopf_fibration(n_points=100, t_range=(-4, 4), phi_range=(0, 2*np.pi)):
    """Generate points for Hopf fibration visualization"""
    t = np.linspace(t_range[0], t_range[1], n_points)
    phi = np.linspace(phi_range[0], phi_range[1], n_points)
    t, phi = np.meshgrid(t, phi)

    # Calculate coordinates on S³
    w = np.cos(t) * np.cos(phi)
    x = np.cos(t) * np.sin(phi)
    y = np.sin(t) * np.cos(phi)
    z = np.sin(t) * np.sin(phi)

    return w, x, y, z

def project_to_3d(w, x, y, z, rotation_angles=(0, 0, 0)):
    """Project 4D points to 3D space with optional rotation"""
    # Normalize points to lie on S³
    norm = np.sqrt(w**2 + x**2 + y**2 + z**2)
    w, x, y, z = w/norm, x/norm, y/norm, z/norm

    # Reshape points for rotation
    original_shape = x.shape
    points = np.stack([x, y, z], axis=-1)
    points_reshaped = points.reshape(-1, 3)

    # Apply rotation
    rot = Rotation.from_euler('xyz', rotation_angles)
    rotated = rot.apply(points_reshaped)

    # Reshape back to original dimensions
    rotated = rotated.reshape(original_shape + (3,))

    # Stereographic projection
    x_proj = rotated[..., 0]/(1 - w)
    y_proj = rotated[..., 1]/(1 - w)
    z_proj = rotated[..., 2]/(1 - w)

    return x_proj, y_proj, z_proj

def compute_field_strength(x, y, z, alpha=1.0):
    """Compute electromagnetic field strength from projected coordinates"""
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z/r)
    phi = np.arctan2(y, x)

    # Field strength decays with distance
    E = alpha * np.exp(-r) * (1 + 0.5*np.sin(theta))
    B = alpha * np.exp(-r) * (1 + 0.5*np.cos(phi))

    return E, B