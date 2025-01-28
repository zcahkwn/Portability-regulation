from pathlib import Path
from portability_env.settings import PLOT_PATH
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def compute_V_star(a1, a2, a3, a4, a6, b1, b3, b4, rI, rG, T, k):
    numerator = a2 * (b1 + b1 * k * rI) + np.sqrt(
        a2
        * (1 + k * rI)
        * (
            -a1 * a3 * b1 * (1 + k * rI)
            + a2 * b1**2 * (1 + k * rI)
            + a1**2 * (b3 - b4 + b3 * k * rI + (a4 - a6 + a4 * k * rI) * T)
        )
    )
    denominator = -a1 * a2 * (1 + k * rI)
    V_star = numerator / denominator
    V_star = np.where((V_star >= -1) & (V_star <= 1), V_star, np.nan)
    return V_star


# Function to plot the equation
def plot_V_star(v_larger_params, v_smaller_params, vbar, save_path=None):
    T = np.linspace(0, 1, 100)  # range of T values

    V_larger = compute_V_star(T=T, **v_larger_params)
    V_smaller = compute_V_star(T=T, **v_smaller_params)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(T, V_larger, label="V > vbar", color="blue")
    ax.plot(T, V_smaller, label="V < vbar", color="orange")
    ax.axhline(vbar, color="green", linestyle="--", label="vbar")
    ax.set_title("Change of V* with respect to T")
    ax.set_xlabel("T")
    ax.set_ylabel("V*")
    ax.legend()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


# Parameters for the lines when V>vbar
v_larger = {
    "a1": 6.8,
    "a2": 5,
    "a3": 0.2,
    "a4": 4.6,
    "a6": 3.5,
    "b1": 2,
    "b3": 3.2,
    "b4": 3.8,
    "rI": 0.3,
    "rG": 0.7,
    "k": 0.6,
}

# Parameters for the lines when V<vbar
v_smaller = {
    "a1": 6.8,
    "a2": 5,
    "a3": 0.2,
    "a4": -1,
    "a6": -0.7,
    "b1": 2,
    "b3": 3.2,
    "b4": 3.8,
    "rI": 0.3,
    "rG": 0.7,
    "k": 0.6,
}


plot_V_star(
    v_larger,
    v_smaller,
    vbar=0.2,
    save_path=PLOT_PATH / "v_star.png",
)
