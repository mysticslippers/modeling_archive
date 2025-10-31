import numpy as np
import matplotlib.pyplot as plt

with open("Данные.txt", encoding="utf-8") as f:
    acf_values = np.array([float(line.replace(',', '.')) for line in f if line.strip()])

lags = np.arange(1, len(acf_values) + 1)

plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 12,
    "axes.edgecolor": "#333",
    "axes.labelcolor": "#333",
    "xtick.color": "#333",
    "ytick.color": "#333",
    "axes.titlesize": 15,
    "axes.titleweight": "bold"
})

plt.figure(figsize=(9, 5))
plt.plot(
    lags, acf_values,
    marker="o", markersize=5, linewidth=1.5, color="#007acc",
    markerfacecolor="white", markeredgecolor="#007acc"
)

plt.xlabel("Сдвиг (k)")
plt.ylabel("Коэффициент автокорреляции")

plt.axhline(0, color="black", linewidth=0.8)
plt.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("acf_graph.png", dpi=300, bbox_inches="tight")
plt.show()
