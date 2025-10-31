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

np.random.seed(42)
n = len(data_given)
data_generated = generate_hyperexp(n, p1, t1, t2)

x_mean = np.mean(data_given)
y_mean = np.mean(data_generated)

numerator = np.sum((data_given - x_mean) * (data_generated - y_mean))
denominator = np.sqrt(np.sum((data_given - x_mean)**2) * np.sum((data_generated - y_mean)**2))

r = numerator / denominator

def interpret_correlation(r):
    if abs(r) < 0.1:
        strength = "очень слабая или отсутствует"
    elif abs(r) < 0.3:
        strength = "слабая"
    elif abs(r) < 0.5:
        strength = "умеренная"
    elif abs(r) < 0.7:
        strength = "заметная"
    elif abs(r) < 0.9:
        strength = "сильная"
    else:
        strength = "очень сильная"

    direction = "прямая" if r > 0 else "обратная"
    return f"{strength} {direction} корреляция"

print(f"Коэффициент корреляции (по формуле Пирсона): r = {r:.6f}")
print("Интерпретация:", interpret_correlation(r))
