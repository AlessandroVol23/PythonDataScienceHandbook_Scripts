import pandas as pd
import numpy as np 

vals1 = np.array([1, None, 3, 4])
print(vals1)

# Notnull and isnull
data = pd.Series([1, np.nan, "hello", None])
print("Data")
print(data)

print("Is null")
print(data.isnull())

print("Not null")
print(data.notnull())

print(data[data.notnull()])