from pathlib import Path
from portability_env.settings import PLOT_PATH
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# When S > sbar


# Function to compute R^B values
def compute_R(b2, a2, b4, a4, b3, rI, a3, a, S, T):
    numerator = (b4 + a4 * S + T * a) * (-b3 + rI - a3 * (b4 + a4 * S + T * a))
    denominator = b2 + a2 * S
    R_B = numerator / denominator
    R_B = np.where((R_B >= 0), R_B, np.nan)
    return R_B


def plot_RB(s_larger, c_to_0, save_path=None):
    T = np.linspace(0, 1, 100)  # range of T values

    S_larger = compute_R(T=T, **s_larger)
    C_to_0 = compute_R(T=T, **c_to_0)
    C_to_inf = compute_R(T=T, **c_to_inf)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(T, S_larger, label="S > sbar", color="blue")
    ax.plot(T, C_to_0, label="S>sbar, C -> 0", color="green")
    ax.plot(T, C_to_inf, label="S>sbar, C -> inf", color="orange", linestyle="--")
    ax.set_title("R^B when S > sbar")
    ax.set_xlabel("T")
    ax.set_ylabel("R^B")
    ax.legend()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    else:
        plt.show()


# Parameters for different lines
s_larger = {
    "b2": 2,
    "a2": 5.5,
    "b4": 0.1,
    "a4": 0.1,
    "b3": 0.1,
    "rI": 0.9,
    "a3": 0.1,
    "a": 0.6,
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
    "a": 0.6,
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
    "a": 0.6,
    "S": 0.5,
}

# Call the function to plot both lines
plot_RB(
    s_larger,
    c_to_0,
    save_path=PLOT_PATH / "s_larger.png",
)
