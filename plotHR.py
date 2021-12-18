import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

filename = '10.1e9y0.0152m.txt'
iDF = pd.read_table(filename, header=13, skipfooter=2, engine='python', delim_whitespace=True)

print(iDF.axes)


# Plot HR-diagram
plt.figure(dpi=300)
plt.plot(10 ** iDF['logTe'], iDF['logL'], '.k')
plt.title(filename[:-4])
plt.grid()
plt.xlim(7000,2000)
plt.xlabel('Effective temperature')
plt.ylabel('Log L/L_sun')
# Sun properties
plt.axvline(5772, ymin=0, ymax=1, linestyle='--', color='r')
plt.axhline(0, xmin=0, xmax=1, linestyle='--', color='r')
# Testing for exact values
#plt.axvline(8050, ymin=0, ymax=1, linestyle='--', color='b')
#plt.axhline(0.82, xmin=0, xmax=1, linestyle='--', color='b')
plt.show()

