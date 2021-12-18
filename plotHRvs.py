import pandas as pd
from matplotlib import pyplot as plt

filename = ['10.1e9y0.0152m.txt', '4.69e9y0.0152m.txt']
i1DF = pd.read_table(filename[0], header=13, skipfooter=2, engine='python', delim_whitespace=True)

i2DF = pd.read_table(filename[1], header=13, skipfooter=2, engine='python', delim_whitespace=True)

# Plot HR-diagram
plt.figure(dpi=300)
plt.plot(10 ** i1DF['logTe'], i1DF['logL'], '.k', label=filename[0][0:6])
plt.plot(10 ** i2DF['logTe'], i2DF['logL'], '.b', label=filename[1][0:6])
plt.legend()
plt.title(filename[0][:-4] + ' vs ' + filename[1][:-4])
plt.grid()
plt.xlim(8500,2000)
plt.xlabel('Effective temperature')
plt.ylabel('Log L/L_sun')
# Sun properties
plt.axvline(5772, ymin=0, ymax=1, linestyle='--', color='r')
plt.axhline(0, xmin=0, xmax=1, linestyle='--', color='r')
plt.show()
