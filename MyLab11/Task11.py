import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

x = np.linspace(-10, 10, 100)

y_1 = np.log(2*x)/np.log(1)
y_2 = np.log2(2*x)
y_3 = np.log(2*x)/np.log(3)
y_4 = np.log(2*x)/np.log(6)

fig, ax = plt.subplots(figsize=(8, 6))

ax.set_title("Графики из задания № 7", fontsize=16)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)

ax.grid(which="major", linewidth=1.2)
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)

ax.plot(x, y_1, c="red", label="log1(2x)")
ax.plot(x, y_2, c="blue", label="log2(2x)")
ax.plot(x, y_3, c="green", label="log4(2x)")
ax.plot(x, y_4, c="black", label="log6(2x)")
ax.legend()

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)

fig.subplots_adjust()

plt.show()
plt.close()