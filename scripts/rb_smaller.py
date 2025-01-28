from pathlib import Path
from portability_env.settings import PLOT_PATH
import numpy as np
import matplotlib.pyplot as plt


# Function to compute R^B values
def compute_R(b2, a2, b4, a4, b3, rI, a3, a, S, T):
    numerator = (b4 + a4 * S + T * a) * (-b3 + rI - a3 * (b4 + a4 * S + T * a))
    denominator = b2 + a2 * S
    R_B = numerator / denominator
    R_B = np.where((R_B >= 0), R_B, np.nan)
    return R_B


# Function to plot R^B for given parameter sets
def plot_RB(params_1, params_2, label_1, label_2, save_path=None):
    T = np.linspace(0, 1, 100)  # range of T values

    values_1 = compute_R(T=T, **params_1)
    values_2 = compute_R(T=T, **params_2)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(T, values_1, label=label_1, color="blue")
    ax.plot(T, values_2, label=label_2, linestyle="--")
    ax.set_title("R^B when S < sbar")
    ax.set_xlabel("T")
    ax.set_ylabel("R^B")
    ax.legend()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    else:
        plt.show()


s_smaller = {
    "b2": 2,
    "a2": 5.5,
    "b4": 0.1,
    "a4": 0.1,
    "b3": 0.1,
    "rI": 0.9,
    "a3": 0.1,
    "a": -0.6,
    "S": 0.5,
}

c_to_0 = {
    "b2": 0.0001,
    "a2": 0.0001,
    "b4": 0.1,
    "a4": 0.1,
    "b3": 0.1,
    "rI": 0.9,
    "a3": 0.1,
    "a": -0.6,
    "S": 0.5,
}

c_to_inf = {
    "b2": 100,
    "a2": 100,
    "b4": 0.1,
    "a4": 0.1,
    "b3": 0.1,
    "rI": 0.9,
    "a3": 0.1,
    "a": -0.6,
    "S": 0.5,
}

d_to_0 = {
    "b2": 2,
    "a2": 5.5,
    "b4": 0.001,
    "a4": 0,
    "b3": 0.1,
    "rI": 0.9,
    "a3": 0.1,
    "a": 0,
    "S": 0.5,
}

plot_RB(
    s_smaller,
    c_to_0,
    "S < sbar",
    "S < sbar, C -> 0",
    save_path=PLOT_PATH / "s_smaller_c_0.png",
)

plot_RB(
    s_smaller,
    c_to_inf,
    "S < sbar",
    "S < sbar, C -> inf",
    save_path=PLOT_PATH / "s_smaller_c_inf.png",
)

plot_RB(
    s_smaller,
    d_to_0,
    "S < sbar",
    "S < sbar, D -> 0",
    save_path=PLOT_PATH / "s_smaller_d_0.png",
)
