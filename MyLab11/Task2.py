import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

data1 = pd.read_csv('Sigma.csv', delimiter=';')
r = data1['r']
y = data1['Sigma']

data2 = np.loadtxt('lambda.csv', delimiter= ';', skiprows= 1)
rr = data2[:, 0]
yy = data2[:, 1]

data3 = pd.read_csv('Vfi.csv', delimiter=';')
rrr = data3['r']
yyy = data3['Vfi']

fig, ax = plt.subplots(figsize=(8, 6))

ax.set_xlabel("r", fontsize=14)
ax.set_ylabel("y", fontsize=14)

ax.grid(which="major", linewidth=1.2)
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)

ax.plot(r, y, c="red", label="Sigma(r)")
ax.plot(rr, yy, 'b--', label="Lambda(r)")
ax.plot(rrr, yyy, c="green", label="Vfi(r)")

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)

ax.legend()

fig.subplots_adjust()

plt.show()
plt.close()