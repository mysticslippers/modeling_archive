import matplotlib.pyplot as plt
import numpy as np

p1 = 0.384
t1 = 42.651
t2 = 0.015

def generate_hyperexp(n, p1, t1, t2):
    u1 = np.random.rand(n)
    u2 = np.random.rand(n)
    return np.where(u1 < p1, -np.log(u2) * t1, -np.log(u2) * t2)

with open("Данные.txt", encoding="utf-8") as f:
    data_given = np.array([float(x.replace(",", ".")) for x in f.read().split() if x.strip()])

n = len(data_given)
np.random.seed(42)
data_generated = generate_hyperexp(n, p1, t1, t2)

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

plt.figure(figsize=(10, 6))

bins = np.linspace(
    min(np.min(data_given), np.min(data_generated)),
    max(np.max(data_given), np.max(data_generated)),
    30
)

plt.hist(data_given, bins=bins, color="#007acc", alpha=0.6, label="Заданная последовательность", edgecolor="white")

plt.hist(data_generated, bins=bins, color="#ff6600", alpha=0.5, label="Сгенерированная последовательность", edgecolor="white")

plt.xlabel("Интервалы значений")
plt.ylabel("Частота")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("hist_compare_given_vs_generated.png", dpi=300, bbox_inches="tight")
plt.show()
