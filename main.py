import streamlit as st
import numpy as np
from hopf_utils import generate_hopf_fibration, project_to_3d, compute_field_strength, generate_toroidal_flow
from field_projections import wave_function_9d, project_to_4d, compute_em_fields
from visualization import (create_hopf_visualization, create_field_lines, 
                         create_wave_function_plot, create_toroidal_flow_visualization)

st.set_page_config(layout="wide")
st.title("9D Hopf Fibration & Field Visualization")

st.sidebar.header("Parameters")

# Hopf fibration parameters
st.sidebar.subheader("Hopf Fibration")
n_points = st.sidebar.slider("Number of points", 20, 200, 100)
rotation_x = st.sidebar.slider("X rotation", -180, 180, 0)
rotation_y = st.sidebar.slider("Y rotation", -180, 180, 0)
rotation_z = st.sidebar.slider("Z rotation", -180, 180, 0)

# Wave function parameters
st.sidebar.subheader("Wave Function")
alpha = st.sidebar.slider("Scale parameter (α)", 0.1, 2.0, 0.5)
rho = st.sidebar.slider("Resonance (ρ)", 0.1, 2.0, 1.0)
p1 = st.sidebar.slider("Polarity 1 (p₁)", -np.pi, np.pi, 0.0)
p2 = st.sidebar.slider("Polarity 2 (p₂)", -np.pi, np.pi, np.pi/2)

# Toroidal flow parameters
st.sidebar.subheader("Toroidal Flow")
n_layers = st.sidebar.slider("Number of nested tori", 1, 5, 3)
flow_density = st.sidebar.slider("Flow visualization density", 10, 50, 20)

# Generate Hopf fibration
w, x, y, z = generate_hopf_fibration(n_points)
x_proj, y_proj, z_proj = project_to_3d(w, x, y, z, 
                                      (np.radians(rotation_x), 
                                       np.radians(rotation_y), 
                                       np.radians(rotation_z)))

# Compute field strength and toroidal flows
E, B = compute_field_strength(x_proj, y_proj, z_proj, alpha)
vx, vy, vz = generate_toroidal_flow(x_proj, y_proj, z_proj, n_layers)

# Create main layout
col1, col2 = st.columns(2)

with col1:
    st.header("Hopf Fibration")
    fig_hopf = create_hopf_visualization(x_proj, y_proj, z_proj, E)
    st.plotly_chart(fig_hopf, use_container_width=True)

    st.header("Toroidal Energy Flows")
    fig_flow = create_toroidal_flow_visualization(x_proj, y_proj, z_proj, 
                                                vx, vy, vz, flow_density)
    st.plotly_chart(fig_flow, use_container_width=True)

with col2:
    st.header("Electromagnetic Fields")
    # Generate 4D projection
    psi_4d = project_to_4d()
    E_field, B_field = compute_em_fields(psi_4d)

    fig_fields = create_field_lines(*E_field, *B_field)
    st.plotly_chart(fig_fields, use_container_width=True)

    st.header("Wave Function")
    fig_wave = create_wave_function_plot(psi_4d)
    st.plotly_chart(fig_wave, use_container_width=True)

st.markdown("""
### Mathematical Foundations & Fundamental Forces

#### 1. Hopf Fibration Equations
The 9D Hopf fibration is described by the mapping S⁸ → S⁴ with fiber S³. The fundamental equations are:

$\\Phi: S^8 \\rightarrow S^4$

For coordinates $(z_1, z_2, z_3, z_4) \\in \\mathbb{C}^4 \\cong \\mathbb{R}^8$, the fibration is given by:

$h(z_1, z_2, z_3, z_4) = (2(z_1\\bar{z_2} + z_3\\bar{z_4}), |z_1|^2 + |z_3|^2 - |z_2|^2 - |z_4|^2)$

#### 2. Wave Function & Quantum States
The 9D wave function $\\Psi$ incorporates both spatial and internal symmetry dimensions:

$\\Psi(\\mathbf{x}, t) = R(r)Y_{lm}(\\theta, \\phi)T(\\alpha, \\beta, \\gamma)e^{-iEt/\\hbar}$

where:
- $R(r)$ is the radial function
- $Y_{lm}$ are spherical harmonics
- $T(\\alpha, \\beta, \\gamma)$ represents internal symmetries
- $E$ is the energy eigenvalue

#### 3. Electromagnetic Field Emergence
The electromagnetic fields emerge from the projection of the Hopf fibration through:

$F_{\\mu\\nu} = \\partial_{\\mu}A_{\\nu} - \\partial_{\\nu}A_{\\mu}$

where the potential $A_{\\mu}$ is derived from the fibration projection:

$A_{\\mu} = \\frac{i}{2}(\\bar{\\psi}\\partial_{\\mu}\\psi - \\psi\\partial_{\\mu}\\bar{\\psi})$

#### 4. Toroidal Flow Dynamics
The toroidal flows represent energy circulation patterns described by:

$\\mathbf{v}(\\mathbf{r}) = \\nabla \\times (\\psi\\mathbf{B}) + \\nabla \\times \\nabla \\times (\\phi\\mathbf{B})$

where:
- $\\psi$ is the poloidal flux function
- $\\phi$ is the toroidal flux function
- $\\mathbf{B}$ is the background magnetic field

#### 5. Fundamental Forces
The four fundamental forces emerge through symmetry breaking of the higher-dimensional structure:

1. **Electromagnetic Force**:
   $U(1)$ symmetry: $F_{em} \\propto \\frac{q_1q_2}{r^2}$

2. **Strong Nuclear Force**:
   $SU(3)$ symmetry: $V_{strong}(r) = -\\frac{\\alpha_s\\hbar c}{r} + kr$

3. **Weak Nuclear Force**:
   $SU(2)$ symmetry: $F_{weak} \\propto G_F(\\bar{\\psi}\\gamma^\\mu\\psi)(\\bar{\\psi}\\gamma_\\mu\\psi)$

4. **Gravitational Force**:
   Emergent from metric distortions: $F_g = -G\\frac{m_1m_2}{r^2}$

#### Interactive Visualization Controls
Use the sidebar controls to explore:
- Rotation angles for different projections of the Hopf fibration
- Wave function parameters affecting field strengths
- Toroidal flow characteristics and nested structures
- Field visualization density and scale parameters

The visualizations above demonstrate how these mathematical structures give rise to observable physical phenomena through dimensional reduction and symmetry breaking.
""")