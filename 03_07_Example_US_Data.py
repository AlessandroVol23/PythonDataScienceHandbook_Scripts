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


pop = pd.read_csv('data/data-USstates-master/state-population.csv')
areas = pd.read_csv('data/data-USstates-master/state-areas.csv')
abbrevs = pd.read_csv('data/data-USstates-master/state-abbrevs.csv')

print(display("pop.head()", "areas.head()", "abbrevs.head()"))

merged = df_abbrevs_pop = pd.merge(pop, abbrevs, left_on='state/region', right_on='abbreviation', how='outer')
merged = merged.drop('abbreviation', 1)
print(merged.head())

# Check if anything is null
print(merged.isnull().any())

# Some in population and state are null
# Lets check which ones
print(merged[merged['population'].isnull()].head())

# Which states are empty? Was missing in abbrevs file
print(merged.loc[merged['state'].isnull(), 'state/region'].unique())
merged.loc[merged["state/region"] == "PR", "state"] = "Puerto Rico"

merged.loc[merged["state/region"] == "USA", "state"] = "United States"

print("state nulls solved")
print(merged.isnull().any())

final = pd.merge(merged, areas, on="state", how="left")
print(final.head())

# Check if something is null
print(final.isnull().any())

# Check why area is sometimes null
print(final['state'][final['area (sq. mi)'].isnull()].unique())

final.dropna(inplace=True)
print(final.head())

data2010 = final.query("year == 2010 & ages == 'total'")
print("\n\n\nQUERY:")
print(data2010.head())

data2010.set_index('state', inplace=True)
density = data2010["population"] / data2010["area (sq. mi)"]
density.sort_values(ascending=False, inplace=True)
density.head()
print("\n\n\n Density:")

print(density)

print("\n\n\n End of the list")
print(density.tail())