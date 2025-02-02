import plotly.graph_objects as go
import numpy as np

def create_hopf_visualization(x, y, z, field_strength, colorscale='Viridis'):
    """Create interactive 3D visualization of Hopf fibration"""
    fig = go.Figure(data=[go.Surface(
        x=x, y=y, z=z,
        surfacecolor=field_strength,
        colorscale=colorscale,
        colorbar=dict(title='Field Strength')
    )])
    
    fig.update_layout(
        title='Hopf Fibration Visualization',
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),
        width=800,
        height=800
    )
    
    return fig

def create_field_lines(Ex, Ey, Ez, Bx, By, Bz, density=10):
    """Create visualization of electromagnetic field lines"""
    x = np.linspace(-5, 5, density)
    y = np.linspace(-5, 5, density)
    z = np.linspace(-5, 5, density)
    X, Y, Z = np.meshgrid(x, y, z)
    
    fig = go.Figure()
    
    # Electric field lines
    fig.add_trace(go.Cone(
        x=X.flatten(),
        y=Y.flatten(),
        z=Z.flatten(),
        u=Ex.flatten(),
        v=Ey.flatten(),
        w=Ez.flatten(),
        colorscale='Reds',
        name='Electric Field'
    ))
    
    # Magnetic field lines
    fig.add_trace(go.Cone(
        x=X.flatten(),
        y=Y.flatten(),
        z=Z.flatten(),
        u=Bx.flatten(),
        v=By.flatten(),
        w=Bz.flatten(),
        colorscale='Blues',
        name='Magnetic Field'
    ))
    
    fig.update_layout(
        title='Electromagnetic Field Lines',
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),
        width=800,
        height=800
    )
    
    return fig

def create_wave_function_plot(psi_4d):
    """Create visualization of wave function magnitude"""
    fig = go.Figure(data=[go.Volume(
        x=np.arange(psi_4d.shape[0]),
        y=np.arange(psi_4d.shape[1]),
        z=np.arange(psi_4d.shape[2]),
        value=np.abs(psi_4d[:,:,:,0]),
        opacity=0.3,
        surface_count=15,
        colorscale='Viridis'
    )])
    
    fig.update_layout(
        title='Wave Function Magnitude',
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),
        width=800,
        height=800
    )
    
    return fig
