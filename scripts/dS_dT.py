from pathlib import Path
from portability_env.settings import PLOT_PATH
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def compute_S_star(b2, a2, b4, a4, b3, rI, a3, a1, T):
    numerator = -a3 * a4 * b2 + np.sqrt(
        a3
        * (a4 * b2 - a2 * (b4 + a1 * T))
        * (a3 * a4 * b2 + a2 * (-b3 + rI) - a2 * a3 * (b4 + a1 * T))
    )
    denominator = a2 * a3 * a4
    S_star = numerator / denominator
    S_star = np.where((S_star >= -1) & (S_star <= 1), S_star, np.nan)
    return S_star


# Function to plot the equation for multiple parameter sets
def plot_S_star(s_larger_params, s_smaller_params, sbar, save_path=None):
    T = np.linspace(0, 1, 100)  # range of T values

    S_larger = compute_S_star(T=T, **s_larger_params)
    S_smaller = compute_S_star(T=T, **s_smaller_params)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(T, S_larger, label="S > sbar", color="blue")
    ax.plot(T, S_smaller, label="S < sbar", color="orange")
    ax.axhline(sbar, color="green", linestyle="--", label="sbar")
    ax.set_title("Change of S* with respect to T")
    ax.set_xlabel("T")
    ax.set_ylabel("S*")
    ax.legend()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Plot saved to {save_path}")
    else:
        plt.show()


# Parameters for the lines when S>sbar
s_larger = {
    "b2": 3,
    "a2": 0.1,
    "b4": 0.2,
    "a4": 4.6,
    "b3": 0.2,
    "rI": 0.8,
    "a3": 0.6,
    "a1": 3.5,
}

# Parameters for the lines when S<sbar
s_smaller = {
    "b2": 3,
    "a2": 0.1,
    "b4": 0.2,
    "a4": 4.6,
    "b3": 0.2,
    "rI": 0.8,
    "a3": 0.6,
    "a1": -1,
}


plot_S_star(
    s_larger,
    s_smaller,
    sbar=0.2,
    save_path=PLOT_PATH / "s_star.png",
)
