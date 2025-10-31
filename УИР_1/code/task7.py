import numpy as np
import matplotlib.pyplot as plt

p1 = 0.384
t1 = 42.651
t2 = 0.015

def generate_hyperexp(n, p1, t1, t2):
    u1 = np.random.rand(n)
    u2 = np.random.rand(n)
    return np.where(u1 < p1, -np.log(u2) * t1, -np.log(u2) * t2)

def autocorrelation_excel(x, max_lag):
    x = np.array(x)
    n = len(x)
    x = x - np.mean(x)
    acf = []
    for lag in range(max_lag + 1):
        num = np.sum(x[:n - lag] * x[lag:])
        den = np.sum(x ** 2)
        acf.append(num / den)
    return np.array(acf)

with open("Данные.txt", encoding="utf-8") as f:
    data_given = np.array([float(x.replace(",", ".")) for x in f.read().split() if x.strip()])

np.random.seed(42)
n = len(data_given)
data_generated = generate_hyperexp(n, p1, t1, t2)

max_lag = 10
acf_given = autocorrelation_excel(data_given, max_lag)
acf_generated = autocorrelation_excel(data_generated, max_lag)

rel_error = np.abs((acf_generated - acf_given) / acf_given) * 100
rel_error[np.isinf(rel_error)] = np.nan

lags = np.arange(max_lag + 1)

plt.style.use("seaborn-v0_8-whitegrid")
plt.figure(figsize=(10, 6))
plt.plot(lags, acf_given, marker="o", label="Заданная последовательность", color="#007acc", linewidth=2)
plt.plot(lags, acf_generated, marker="s", label="Сгенерированная последовательность", color="#ff6600", linewidth=2, alpha=0.8)
plt.xlabel("Лаг")
plt.ylabel("Коэффициент автокорреляции")
plt.title("Сравнение автокорреляционных функций (по формуле Excel)\nдля заданной и сгенерированной последовательностей")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("acf_compare_excel_formula.png", dpi=300, bbox_inches="tight")
plt.show()

print("Относительная погрешность автокорреляции (в %) для 10 шагов:")
for lag, err in enumerate(rel_error):
    if not np.isnan(err):
        print(f"Лаг {lag}: {err:.3f}%")
    else:
        print(f"Лаг {lag}: деление на ноль (ACF заданной последовательности ≈ 0)")
