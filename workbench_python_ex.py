import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1) Create data
np.random.seed(42)
n = 120
df = pd.DataFrame({
    "day": pd.date_range("2026-01-01", periods=n, freq="D"),
    "sales": np.random.normal(loc=200, scale=25, size=n).round(0)
})

# 2) Transform (two easy steps)
df["sales"] = df["sales"].clip(lower=0)                  # remove negative values
df["sales_7d_avg"] = df["sales"].rolling(7).mean()      # 7-day moving average

# 3) Graph
plt.figure(figsize=(10, 5))
plt.plot(df["day"], df["sales"], label="Daily sales")
plt.plot(df["day"], df["sales_7d_avg"], label="7-day avg")
plt.title("Sales Over Time")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.legend()
plt.tight_layout()

# 4) Export graph
out_file = "sales_plot.png"
plt.savefig(out_file, dpi=200)
plt.close()

print(f"Saved chart to: {out_file}")
