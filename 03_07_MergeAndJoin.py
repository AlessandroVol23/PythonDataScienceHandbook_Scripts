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

# One-to-one-join
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
print(display('df1', 'df2'))
df3 = pd.merge(df1, df2)
print(df3)

# Many-to-one join
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                    'supervisor': ['Carly', 'Guido', 'Steve']})

print(display("df3", "df4", "pd.merge(df3, df4)"))

# Many-to-many joins
df5 = pd.DataFrame({'group': ['Accounting', 'Accounting',
                              'Engineering', 'Engineering', 'HR', 'HR'],
                    'skills': ['math', 'spreadsheets', 'coding', 'linux',
                               'spreadsheets', 'organization']})
print(df5)

print(display("df1", "df5", "pd.merge(df1, df5)"))

# On keyword

print(display("df1", "df2", "pd.merge(df1, df2, on='employee')"))

# Left on and right on keyword
df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})
print("df3")
print(df3)
print("df1")
print(df1)

print(display("df1", "df3", "pd.merge(df1, df3, left_on='employee', right_on='name')"))

# Drop redundant column
df6 = pd.merge(df1, df3, left_on='employee', right_on='name').drop('name', axis=1)
print("DF6")
print(df6)

# left index and right index
df1a = df1.set_index("employee")
df2a = df2.set_index("employee")
print(display("df1a", "df2a"))

print(display("df1a", "df2a", "pd.merge(df1a, df2a, left_index=True, right_index=True)"))

# Joins Data Frame methode
print(display("df1a", "df2a", "df1a.join(df2a)"))

# Arithmetic Joins
df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']},
                   columns=['name', 'food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['wine', 'beer']},
                   columns=['name', 'drink'])
print(display("df6", "df7", "pd.merge(df6, df7)"))

print(display("pd.merge(df6, df7, how='inner')"))

print(display("pd.merge(df6, df7, how='outer')"))

print(display("pd.merge(df6, df7, how='left')"))

print(display("pd.merge(df6, df7, how='right')"))

# Overlapping column names
df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [1, 2, 3, 4]})
df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [3, 1, 4, 2]})
print(display('df8', 'df9', "pd.merge(df8, df9, on='name')"))

print(display('df8', 'df9', "pd.merge(df8, df9, on='name', suffixes=['_ERSTER', '_ZWOATER'], sort=True)"))
