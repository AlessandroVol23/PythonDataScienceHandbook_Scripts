import pandas as pd 
import numpy as np 

# Bad way:

index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
               18976457, 19378102,
               20851820, 25145561]
pop = pd.Series(populations, index=index)
print(pop)


index = pd.MultiIndex.from_tuples(index)
print(index)

pop = pop.reindex(index)
print("POP")
print(pop)
print("POP 2010")
print(pop[:, 2010])

# Multi Index into another dimension
pop_df = pop.unstack()
print("POP DF")
print(pop_df)

# Back to normal
pop_df = pop_df.stack()
print("Pop df stack")
print(pop_df)

# More Dimensions
pop_df = pd.DataFrame({'total': pop,
                       'under18': [9267089, 9284094,
                                   4687374, 4318033,
                                   5906301, 6879014]})

print("Pop df with more dimensions:")
print(pop_df)

# Ufuncs
f_u18 = pop_df["under18"] / pop_df["total"]
f_u18 = f_u18.unstack()
print("F_u18")
print(f_u18)

# Automatic creation of Multiindex dataframes 

df = pd.DataFrame(np.random.rand(4,2), index = [["a", "a", "b", "b"], [1, 2, 1, 2]], columns=["data1", "data"])
print("Multiindex df")
print(df)

# Explicit Multiindex creation

mi = pd.MultiIndex.from_arrays([["a", "a", "b", "b"], [1, 2, 1, 2]])
print("Explizit Multinindex")
print(mi)

# You can get it from arrays / tuples / cartesian products
pop.index.names = ["state", "year"]
print(pop)

# Multiindexing for columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names=["year", "visit"])

columns = pd.MultiIndex.from_product([["bob", "guido", "sue"], ["HR", "temp"]], names=["subject", "type"])

# mock some data
data = np.round(np.random.randn(4,6) , 1)
data[:, ::2] *= 10
data += 37

# create the data frame
health_data = pd.DataFrame(data, index=index, columns=columns)
print("Health Data:")
print(health_data)

# Just get guidos data
print("health_data[guido]")
print(health_data["guido"])