import numpy as np 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn;  # set plot styles
import pandas as pd

seaborn.set()


# use pandas to extract rainfall inches as a NumPy array
path = "../notebooks/data/Seattle2014.csv"
rainfall = pd.read_csv(path)['PRCP'].values
inches = rainfall / 254.0  # 1/10mm -> inches
inches.shape

plt.hist(inches, 40);
# plt.show(block=True)

print("Number days without rain:            ", np.sum(inches == 0))
print("Number days with rain:               ", np.sum(inches != 0))
print("Days with more than 0.5 inches:      ", np.sum(inches > 0.5))
print("Rainy days with < 0.2 inches:        ", np.sum((inches > 0) & (inches < 0.2)))

# MASKING...

# construct a mask of all rainy days
rainy = (inches > 0)

# construct a mask of all summer days (June 21st is the 172nd day)
days = np.arange(365)
summer = (days > 172) & (days < 262)

print("Median precip on rainy days in 2014 (inches):    ", np.median(inches[rainy]))

print("Median precip on summer days in 2014 (inches):   ", np.median(inches[summer]))

print("Maximum precip on summer days in 2014 (inches):  ", np.max(inches[summer]))

print("Median precip on non-summer rainy days (inches): ", np.median(inches[rainy & ~summer]))

