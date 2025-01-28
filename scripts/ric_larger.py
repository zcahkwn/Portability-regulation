from pathlib import Path
from portability_env.settings import PLOT_PATH
import numpy as np
import matplotlib.pyplot as plt


# Function to compute R^IC values
def compute_R(a1, a2, a3, a4, a6, b1, b3, b4, rI, rG, T, k, V):
    numerator = (
        b3
        - b4
        + b1 * rG
        + b3 * k * rI
        + V * (a3 + a1 * rG + a3 * k * rI + a2 * (1 + k * rI) * V)
        + (T + k * rI * T) * a4
        - T * a6
    )
    denominator = b1 + a1 * V
    R_IC = numerator / denominator
    R_IC = np.where((R_IC >= 0), R_IC, np.nan)
    return R_IC


# Function to plot R^IC for given parameter sets
def plot_RIC(params_1, params_2, label_1, label_2, save_path=None):
    T = np.linspace(0, 1, 100)  # range of T values

    values_1 = compute_R(T=T, **params_1)
    values_2 = compute_R(T=T, **params_2)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(T, values_1, label=label_1, color="blue")
    ax.plot(T, values_2, label=label_2, linestyle="--")
    ax.set_title("R^IC when V > vbar")
    ax.set_xlabel("T")
    ax.set_ylabel("R^IC")
    ax.legend()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    else:
        plt.show()


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
    "V": 0.5,
}

c_to_0 = {
    "a1": 0,
    "a2": 5,
    "a3": 0.2,
    "a4": 4.6,
    "a6": 3.5,
    "b1": 0.001,
    "b3": 3.2,
    "b4": 3.8,
    "rI": 0.3,
    "rG": 0.7,
    "k": 0.6,
    "V": 0.5,
}

c_to_inf = {
    "a1": 100,
    "a2": 5,
    "a3": 0.2,
    "a4": 4.6,
    "a6": 3.5,
    "b1": 100,
    "b3": 3.2,
    "b4": 3.8,
    "rI": 0.3,
    "rG": 0.7,
    "k": 0.6,
    "V": 0.5,
}


plot_RIC(
    v_larger,
    c_to_0,
    "V > vbar",
    "V > vbar, C -> 0",
    save_path=PLOT_PATH / "v_larger_c_0.png",
)

plot_RIC(
    v_larger,
    c_to_inf,
    "V > vbar",
    "V > vbar, C -> inf",
    save_path=PLOT_PATH / "v_larger_c_inf.png",
)
