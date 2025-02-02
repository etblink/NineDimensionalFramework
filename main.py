import streamlit as st
import numpy as np
from hopf_utils import generate_hopf_fibration, project_to_3d, compute_field_strength
from field_projections import wave_function_9d, project_to_4d, compute_em_fields
from visualization import create_hopf_visualization, create_field_lines, create_wave_function_plot

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

# Generate Hopf fibration
w, x, y, z = generate_hopf_fibration(n_points)
x_proj, y_proj, z_proj = project_to_3d(w, x, y, z, 
                                      (np.radians(rotation_x), 
                                       np.radians(rotation_y), 
                                       np.radians(rotation_z)))

# Compute field strength
E, B = compute_field_strength(x_proj, y_proj, z_proj, alpha)

# Create main layout
col1, col2 = st.columns(2)

with col1:
    st.header("Hopf Fibration")
    fig_hopf = create_hopf_visualization(x_proj, y_proj, z_proj, E)
    st.plotly_chart(fig_hopf, use_container_width=True)

    st.header("Key Equations")
    st.latex(r"\text{9D Wave Function:}")
    st.latex(r"\Psi(x_1,x_2,x_3,\nu,\alpha,\rho,p_1,p_2,\Omega) \in \mathbb{C}")
    st.latex(r"\text{Projection to 4D:}")
    st.latex(r"\Psi_{4D}(r,\theta,\phi,t) = \int \Psi \, d\nu \, d\alpha \, d\rho \, dp_1 \, dp_2 \, d\Omega")

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
### About this Visualization
This tool visualizes the 9-dimensional Hopf fibration model and its projections to observable physics:

1. **Hopf Fibration**: Shows the projection of the higher-dimensional structure to 3D space
2. **Electromagnetic Fields**: Displays the emergent electromagnetic field structure
3. **Wave Function**: Visualizes the magnitude of the projected wave function

Use the sidebar controls to adjust various parameters and explore how they affect the visualizations.
""")
