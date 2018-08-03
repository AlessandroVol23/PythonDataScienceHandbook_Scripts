import numpy as np 
import pandas as pd 

def make_df(cols, ind):
    data = {c: [str(c) + str(i) for i in ind]
                for c in cols}
    return pd.DataFrame(data, ind)



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


df = make_df("ABC", range(3))
print(df)

# Concatination in Pandas

ser1 = pd.Series(["A", "B", "C"], index=[1,2,3])
print("Series 1")
print(ser1)

ser2 = pd.Series(["D", "E", "F"], index=[4, 5, 6])
print("Series 1 and 2 concatted")
print(pd.concat([ser1, ser2]))

df1 = make_df("AB", [1,2])
df2 = make_df("AB", [3,4])
print(display('df1', 'df2', 'pd.concat([df1, df2])'))

df3 = make_df("AB", [0,1])
df4 = make_df("CD", [0,1])
print(display("df3", "df4", "pd.concat([df3, df4], axis=1)"))

# Duplicate indices
x = make_df("AB", [0,1])
y = make_df("AB", [2,3])
y.index = x.index 
print(display("x", "y", "pd.concat([x, y])"))

# Verify integrity
try:
    pd.concat([x, y], verify_integrity=True)
except ValueError as e:
    print("Value Error", e)

# Ignoring the index
print("Ignoring the index")
print(display("x", "y", "pd.concat([x, y], ignore_index=True)"))

# Adding Multiindex keys
print(display("x", "y", "pd.concat([x, y], keys=['x', 'y'])"))

# Joins
df5 = make_df("ABC", [1,2])
df6 = make_df("BCD", [3, 4])
print(display("df5", "df6", "pd.concat([df5, df6])"))

# Inner Join
print(display("df5", "df6", "pd.concat([df5, df6], join='inner')"))

# JOin Axes
print(display("df5", "df6", "pd.concat([df5, df6], join_axes=[df5.columns])"))
