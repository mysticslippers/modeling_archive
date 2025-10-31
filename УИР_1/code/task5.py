import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

p1 = 0.384
t1 = 42.651
t2 = 0.015

sample_sizes = [10, 20, 50, 100, 200, 300]

def generate_hyperexp(n, p1, t1, t2):
    u1 = np.random.rand(n)
    u2 = np.random.rand(n)
    return np.where(u1 < p1, -np.log(u2) * t1, -np.log(u2) * t2)

np.random.seed(42)
results = []

for n in sample_sizes:
    values = generate_hyperexp(n, p1, t1, t2)
    mean_val = np.mean(values)
    var_val = np.var(values, ddof=1)
    std_val = np.sqrt(var_val)
    cv_val = std_val / mean_val

    conf_levels = [0.9, 0.95, 0.99]
    conf_intervals = {}
    for p in conf_levels:
        alpha = 1 - p
        t_val = t.ppf(1 - alpha / 2, df=n - 1)
        margin = t_val * std_val / np.sqrt(n)
        conf_intervals[p] = (mean_val - margin, mean_val + margin)

    results.append({
        "n": n,
        "mean": mean_val,
        "var": var_val,
        "std": std_val,
        "cv": cv_val,
        "conf": conf_intervals
    })

print("Результаты генерации гиперэкспоненциальных случайных величин:")
for r in results:
    print(f"\n--- n = {r['n']} ---")
    print(f"Математическое ожидание: {r['mean']:.6f}")
    print(f"Несмещённая дисперсия:   {r['var']:.6f}")
    print(f"Среднеквадратичное отклонение: {r['std']:.6f}")
    print(f"Коэффициент вариации:    {r['cv']:.6f}")
    for p, (low, high) in r['conf'].items():
        print(f"Доверительный интервал p={p:.2f}: [{low:.6f}; {high:.6f}]")


n = 300
values = generate_hyperexp(n, p1, t1, t2)

plt.style.use("seaborn-v0_8-whitegrid")
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 12,
    "axes.edgecolor": "#333333",
    "axes.labelcolor": "#333333",
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "axes.titlesize": 15,
    "axes.titleweight": "bold"
})

plt.figure(figsize=(10, 5))
plt.plot(range(1, len(values) + 1), values,
         marker="o", markersize=4, color="#007acc", linewidth=1.2,
         markerfacecolor="white", markeredgecolor="#007acc")
plt.xlabel("Порядковый номер измерения")
plt.ylabel("Числовое значение")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("graph_hyperexp_n300.png", dpi=300, bbox_inches="tight")
plt.show()

# === Гистограмма распределения ===
plt.figure(figsize=(8, 5))
plt.hist(values, bins=20, color="#007acc", edgecolor="white", alpha=0.85)
plt.xlabel("Интервалы значений")
plt.ylabel("Частота")
plt.grid(axis='y', linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("hist_hyperexp_n300.png", dpi=300, bbox_inches="tight")
plt.show()
