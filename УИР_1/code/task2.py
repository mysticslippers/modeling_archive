import matplotlib.pyplot as plt

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

plt.figure(figsize=(10, 5))
plt.plot(range(1, len(values) + 1), values,
         marker="o", markersize=4, color="#007acc", linewidth=1.5,
         markerfacecolor="white", markeredgecolor="#007acc")
plt.xlabel("Порядковый номер измерения")
plt.ylabel("Числовое значение")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("graph_sequence.png", dpi=300, bbox_inches="tight")
plt.show()
