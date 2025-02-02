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
### About this Visualization
This tool visualizes the 9-dimensional Hopf fibration model and its projections to observable physics:

1. **Hopf Fibration**: Shows the projection of the higher-dimensional structure to 3D space
2. **Toroidal Energy Flows**: Displays nested toroidal vortex structures that represent energy circulation
3. **Electromagnetic Fields**: Shows the emergent electromagnetic field structure
4. **Wave Function**: Visualizes the magnitude of the projected wave function

The toroidal flows represent how energy circulates through the Hopf fibration structure, with nested patterns demonstrating the self-similar, fractal nature of the system. These flows are fundamental to understanding how the 9D structure gives rise to observable physical phenomena.

Use the sidebar controls to adjust various parameters and explore how they affect the visualizations.
""")