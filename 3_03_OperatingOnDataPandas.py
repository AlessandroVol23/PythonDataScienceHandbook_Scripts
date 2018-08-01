import pandas as pd 
import numpy as np 

rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0,10,4))
print(ser)

df = pd.DataFrame(rng.randint(0,10,(3,4)), columns=["A", "B", "C", "D"])
print(df)

print("np.exp(ser):")
print(np.exp(ser))

print(np.sin(df*np.pi/4))

area = pd.Series({"Alaska": 1723337, "Texas": 695662, "California": 423967}, name="area")

population = pd.Series({"California": 38332521, "Texas": 26448193, "New York": 19651127}, name="population")

print()
print(population / area)

A = pd.DataFrame(rng.randint(0,10,(2,2)), columns=list("AB"))
print(A)

B = pd.DataFrame(rng.randint(0, 10, (3, 3)), columns=list("BAC"))
print(B)

print(A+B)

fill = A.stack().mean()
A_new = A.add(B, fill_value=fill)
print(A_new)

# Ufuncs: Operations Between DataFrame and Series
A = rng.randint(10, size=(3,4))
print("A:")
print(A)

print("A[0]:", A[0])
print(A - A[0])

df = pd.DataFrame(A, columns=list("QRST"))
print("DF:")
print(df)

print("df - df.iloc[0]")
print(df - df.iloc[0])

# Column wise
print("Column wise. df.subtract(df[R], axis=0)")
print(df.subtract(df["R"], axis=0))

halfrow = df.iloc[0, ::2]
print("Halfrow")
print(halfrow)

print("DF")
print(df)

print("DF - halfrow")
print(df - halfrow)
