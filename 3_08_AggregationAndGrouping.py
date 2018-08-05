import numpy as np
import pandas as pd


class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""

    def __init__(self, *args):
        self.args = args

    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)

    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)


# Planet mock data
import seaborn as sns
planets = sns.load_dataset('planets')
print(planets.shape)

print(planets.head())

# Simple Aggregations in Pandas
rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
print("\n\nRandom Series")
print(ser)

print("\n\n Series Mean")
print(ser.mean())

df = pd.DataFrame({"A": rng.rand(5),
                   "B": rng.rand(5)})

print("\n\n DF:")
print(df)

print("\n\n Mean DF")
print(df.mean())

print("\n\nMean over columns")
print(df.mean(axis="columns"))

# Describe Data sets just shows different aggregation methods on a data set
print(planets.dropna().describe())

# Group By

df = pd.DataFrame({"key": ["A", "B", "C", "A", "B", "C"],
                   "data": range(6)}, columns=["key", "data"])

print(df)

print(df.groupby("key"))

print(df.groupby("key").sum())

print(planets.groupby("method")["orbital_period"].median())

for (method, group) in planets.groupby("method"):
    print("{0:30s} shape={1}".format(method, group.shape))

print("\n\nDescribe Unstack")
print(planets.groupby("method")["year"].describe().unstack())

# Aggregate, filter, transform, apply

# DataFrame to use
rng = np.random.RandomState(0)
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': rng.randint(0, 10, 6)},
                  columns=['key', 'data1', 'data2'])
print(df)

# Aggregation
print(df.groupby("key").aggregate([min, np.median, max]))

# Aggregation with dictionary mapping
print(df.groupby("key").aggregate({"data1": "min",
                                   "data2": "max"}))

# Filtering


def filterFunc(x):
    return x["data2"].std() > 4


print(display("df", "df.groupby('key').std()",
              "df.groupby('key').filter(filterFunc)"))

# Transformation
print("\n\nTransformation")
print(df.groupby("key").transform(lambda x: x-x.mean()))

# Apply Method


def norm_by_data2(x):
    x["data1"] /= x["data2"].sum()
    return x


print(display("df", "df.groupby('key').apply(norm_by_data2)"))

# Specifying the split key

L = [0, 1, 0, 1, 2, 0]
print(display("df", "df.groupby(L).sum()"))

# Groupin Example
# Get rid of the exact year and just get the decade
decade = 10 * (planets["year"] // 10)
# Cast it to a string and put a at the end of it
decade = decade.astype(str) + "s"
# Give it the name / index decade
decade.name = 'decade'
# Group by method and decade. Sum up the number and unstack
print(planets.groupby(['method', decade])['number'].sum().unstack().fillna(0))
