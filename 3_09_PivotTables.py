import pandas as pd
import numpy as np
import seaborn as sns

titanic = sns.load_dataset('titanic')

# Group by gender and survived
print(titanic.groupby("sex")["survived"].mean())

# Double group by to see classes and gender survived
print(titanic.groupby(["sex", "class"])[
      "survived"].aggregate("mean").unstack())

# Pivot Table
print("\n\nTitanic Pivot")
print(titanic.pivot_table("survived", index="sex", columns="class"))

age = pd.cut(titanic['age'], [0, 18, 80])
print("\n\nSurvived bins age")
print(titanic.pivot_table('survived', ['sex', age], 'class'))

fare = pd.qcut(titanic["fare"], 2)
print("\n\n")
print(titanic.pivot_table("survived", ["sex", age], [fare, "class"]))

# Example aggregation function
print("\n\n")
print(titanic.pivot_table(index="sex", columns="class", aggfunc={
    "survived": sum, "fare": "mean"}))
