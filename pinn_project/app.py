import streamlit as st
import numpy as np
import tensorflow as tf
# import matplotlib.pyplot as plt

st.set_page_config(page_title="PINN Burgers Solver", layout="centered")

st.title("🔬 PINN vs Analytical Solution for Burgers' Equation")

# ℹ️ Display the valid domain
st.markdown("""
ℹ️ The model was trained on the domain:  
- Time (t) ∈ [0, 1]  
- Space (x) ∈ [-1, 1]  
Please enter values within this range.
""")

# Load model from file
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("pinn_model.h5", compile=False)

model = load_model()

# True analytical solution for comparison
def analytical_solution(t, x):
    nu = 0.01 / np.pi
    return -np.sin(np.pi * x) * np.exp(-np.pi**2 * nu * t)

# Sidebar for input
st.sidebar.header("📥 Input Parameters")

# User-defined inputs with domain limits
t_val = st.sidebar.slider("Time t", 0.0, 1.0, 0.5, step=0.01)
x_val = st.sidebar.slider("Space x", -1.0, 1.0, 0.0, step=0.01)

# Predict with the model
tx_input = np.array([[t_val, x_val]])
predicted = model.predict(tx_input, verbose=0)[0, 0]
actual = analytical_solution(t_val, x_val)
error = abs(predicted - actual)

# Show results
st.subheader("📊 Results at selected (t, x):")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="🧠 PINN Prediction", value=f"{predicted:.5f}")
with col2:
    st.metric(label="📐 Analytical Solution", value=f"{actual:.5f}")

st.write(f"❌ Absolute Error: {error:.5e}")

# # Plot u(x) at fixed t
# if st.checkbox("📈 Show u(x) across space at fixed t"):
#     x_vals = np.linspace(-1, 1, 200)
#     t_vals = np.full_like(x_vals, t_val)
#     tx_grid = np.stack([t_vals, x_vals], axis=-1)
#     u_pred = model.predict(tx_grid, verbose=0).flatten()
#     u_true = analytical_solution(t_vals, x_vals)

#     fig, ax = plt.subplots(figsize=(8, 4))
#     ax.plot(x_vals, u_true, "--", label="Analytical", color="black")
#     ax.plot(x_vals, u_pred, label="PINN Prediction", color="blue")
#     ax.set_xlabel("x")
#     ax.set_ylabel("u(t,x)")
#     ax.set_title(f"u(x) at t = {t_val}")
#     ax.legend()
#     st.pyplot(fig)
