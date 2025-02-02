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

#### 1. 9D Wave Function Evolution
The fundamental evolution equation in its most advanced form:

$□_{9D}Ψ + ξR_9(Ψ)Ψ + λ(Ψ)Ψ^3 + η(Ψ)Ψ^5 + α(Ψ)□^2Ψ + ΔΨ_{NP} = ξ_{stoch}(x,t)$

where $□_{9D}$ is the 9D d'Alembert operator, $ξ$ couples the wave function to curvature, $λ(Ψ)$ and $η(Ψ)$ are nonlinear self-interaction couplings, and $ξ_{stoch}(x,t)$ is a stochastic term.

#### 2. Dynamically Adjusted Ricci Scalar
The 9D Ricci scalar incorporates quantum informational content:

$R_9(Ψ) = R_{9AdS} + ζ\\tanh(κΨ) + ϵS_{ent}(x)$

where $S_{ent}(x) = -γ\\ln|Ψ(x)|$

With nonperturbative modifications:

$R_{9NP} = R_9(Ψ) + σ\\sum_ℓ Δℓ^2$

#### 3. Nonperturbative Corrections
Path integral backreaction is represented by:

$ΔΨ_{NP} = \\int e^{-S_{eff}/ℏ}dS_{eff}$

#### 4. 4D Projection & Electromagnetic Fields
The 4D projection of the wave function in spherical coordinates $(r,θ,φ)$ and time $t$:

$Ψ_{4D}(r,θ,φ,t) = \\int Ψ(x_1,x_2,x_3,ν,α,ρ,p_1,p_2,Ω)dνdαdρdp_1dp_2dΩ$

The electromagnetic 4-potential emerges as:

$A_μ = (\\frac{∂Ψ_{4D}}{∂t}, \\nabla Ψ_{4D})$

Leading to the field tensor:

$F_{μν} = ∂_μA_ν - ∂_νA_μ$

#### 5. Unified 9D Lagrangian
The full Lagrangian governing dynamics:

$L_{9D} = -\\frac{1}{4}F_{AB}^aF_a^{AB} + i\\bar{Ψ}Γ^AD_AΨ - m\\bar{Ψ}Ψ + \\frac{1}{16πG_9}R_9 + L_{extra}$

where $L_{extra}$ accounts for extra-dimensional contributions:

$L_{extra} = -\\frac{1}{4}G_{IJ}^bG_b^{IJ} + \\frac{1}{2}(∂_μΦ^b)^2 - V(Φ^b)$

#### 6. Fundamental Forces
The four fundamental forces emerge through symmetry breaking:

1. **Electromagnetic Force** ($U(1)$ symmetry):
   $F_{em} \\propto \\frac{q_1q_2}{r^2}$

2. **Strong Nuclear Force** ($SU(3)$ symmetry):
   $V_{strong}(r) = -\\frac{α_s\\hbar c}{r} + kr$

3. **Weak Nuclear Force** ($SU(2)$ symmetry):
   $F_{weak} \\propto G_F(\\bar{ψ}γ^μψ)(\\bar{ψ}γ_μψ)$

4. **Gravitational Force** (emergent from metric distortions):
   $F_g = -G\\frac{m_1m_2}{r^2}$

#### Interactive Visualization Controls
Use the sidebar controls to explore:
- Rotation angles for different projections of the Hopf fibration
- Wave function parameters affecting field strengths
- Toroidal flow characteristics and nested structures
- Field visualization density and scale parameters

The visualizations above demonstrate how these mathematical structures give rise to observable physical phenomena through dimensional reduction and symmetry breaking.
""")