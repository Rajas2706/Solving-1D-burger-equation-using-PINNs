# 🧠 PINN for Solving 1D Burgers' Equation

This project implements a **Physics-Informed Neural Network (PINN)** using TensorFlow to solve the 1D **viscous Burgers' equation**, a classical nonlinear partial differential equation. It also includes a **Streamlit web app** to compare the PINN solution against the analytical solution.

---

## 🔬 About Burgers' Equation

The 1D viscous Burgers' equation is:

∂u/∂t + u ∂u/∂x = ν ∂²u/∂x²
---
## 📁 Project Structure
```bash
├── training/            # PINN model training
│   ├── main.py          # Training script
│   ├── network.py       # Neural network architecture
│   ├── pinn.py          # PINN model definition
│   ├── layer.py         # Custom gradient layer
│   ├── optimizer.py     # L-BFGS-B optimizer wrapper
│   ├── tf_silent.py     # TensorFlow log suppressor
├── webapp/              # Streamlit app for visualization
│   └── app.py           # Web app script
├── pinn_model.h5        # Trained PINN model
├── requirements.txt     # Python dependencies
├── .gitignore           # Files to exclude from Git

```
## 🧪 About
> The PINN model learns the solution 
u(t,x) of the Burgers' equation:

 ### ∂u/∂t + u ∂u/∂x = ν ∂²u/∂x²
 >where ν is the kinematic viscosity. The neural network is trained with physics constraints encoded as loss functions to satisfy the PDE, initial and boundary conditions.
---
## 🖥️ Installation

> ⚠️ Python 3.8 or higher is recommended.

### 1. Clone the repo

```bash
git clone https://github.com/Rajas2706/Solving-1D-burger-equation-using-PINNs.git
cd Solving-1D-burger-equation-using-PINNs
```
### 2. Create and activate a Python virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install dependencies:
```bash
pip install -r requirements.txt
```
## ⚙️ Usage
### Training the model
#### Navigate to the training/ folder and run:
```bash
python main.py
```
>This trains the PINN model and saves the weights to pinn_model.h5.
## Running the web app
### Launch the Streamlit app to interactively explore predictions:
```bash
streamlit run webapp/app.py
>Open the provided localhost URL in your browser to use the interface.
