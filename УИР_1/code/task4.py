import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

with open("Данные.txt", "r", encoding="utf-8") as f:
    data = f.read().splitlines()

values = [float(x.replace(",", ".")) for x in data if x.strip() != ""]

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

plt.figure(figsize=(8, 5))
plt.hist(values, bins=20, color="#007acc", edgecolor="white", alpha=0.85)
plt.xlabel("Интервалы значений")
plt.ylabel("Частота")
plt.grid(axis='y', linestyle="--", alpha=0.6)
plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(integer=True))  # целые деления
plt.tight_layout()
plt.savefig("histogram_sequence.png", dpi=300, bbox_inches="tight")  # сохраняем график
plt.show()
