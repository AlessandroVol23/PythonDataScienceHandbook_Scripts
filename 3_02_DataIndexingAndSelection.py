import numpy as np
import pandas as pd 

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
print("Data[1]:" , data[1])

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=["a", "b", "c", "d"])
print("Data[b]", data["b"])

print("a" in data)


print(data.keys())

print(data.items())

data["z"] = 2.0

print(data)

data["e"] = 1.5

print(data)

print("Data < 1.0:\n", data[(data < 1.0)])

print("Data between 0.3 and 0.8", data[(data >0.3) & (data < 0.8)])

area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
print("Data /w area and pop:")
print(data)

print("Data[area]\n", data["area"])

print("Date[pop]")
print(data["pop"])

data["density"] = data["pop"] / data["area"]
print("Data with density")
print(data)

print("Data frame as 2d array")
print(data.values)
