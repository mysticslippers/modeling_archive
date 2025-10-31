import numpy as np
from scipy.stats import t

with open("Данные.txt", encoding="utf-8") as f:
    data = [float(x.replace(',', '.')) for x in f.read().split() if x.strip()]

data = np.array(data)
N = len(data)
print(f"Всего считано значений: {N}")

sample_sizes = [10, 20, 50, 100, 200, 300]
sample_sizes = [n for n in sample_sizes if n <= len(data)]

results = []

for n in sample_sizes:
    sample = data[:n]
    mean_val = np.mean(sample)
    var_val = np.var(sample, ddof=1)
    std_val = np.sqrt(var_val)
    cv_val = std_val / abs(mean_val) if mean_val != 0 else np.nan

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

print("\n=== РЕЗУЛЬТАТЫ АНАЛИЗА ===")
for r in results:
    print(f"\n--- n = {r['n']} ---")
    print(f"Математическое ожидание: {r['mean']:.6f}")
    print(f"Несмещённая дисперсия:   {r['var']:.6f}")
    print(f"Среднеквадратичное отклонение: {r['std']:.6f}")
    print(f"Коэффициент вариации:    {r['cv']:.6f}")
    for p, (low, high) in r['conf'].items():
        print(f"Доверительный интервал при p={p:.2f}: [{low:.6f}; {high:.6f}]")
