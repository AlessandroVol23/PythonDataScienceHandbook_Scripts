import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

births = pd.read_csv("data/births.csv")
print(births.head())

# Add decade
births["decade"] = 10 * (births["year"] // 10)
print("\n\n", births.head())
print("\n\n")
print(births.pivot_table("births", index="decade", columns="gender", aggfunc="sum"))

sns.set()
births.pivot_table("births", index="year",
                   columns="gender", aggfunc="sum").plot()
plt.ylabel("total births per year")
# plt.show(block=True)

# Further data exploration
quartiles = np.percentile(births["births"], [25, 50, 75])
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])
print("Quartiles:\n", quartiles)
print("MU:\n", mu)
print("SIG", sig)

births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
print(births.head())

# Set day to int
births["day"] = births["day"].astype(int)

# Create a datetime index
births.index = pd.to_datetime(
    10000 * births.year + 100 * births.month + births.day, format="%Y%m%d")

births["dayofweek"] = births.index.dayofweek

births.pivot_table("births", index="dayofweek",
                   columns="decade", aggfunc="mean").plot()
plt.gca().set_xticklabels(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])
plt.ylabel("mean birthdays by day")
# plt.show(block=True)

births_by_date = births.pivot_table(
    "births", [births.index.month, births.index.day])
print("\n\n", births_by_date)

fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)
plt.show(block=True)
