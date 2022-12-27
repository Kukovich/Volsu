import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

x = np.linspace(-10, 10, 100)

y_1 = (x**2)*np.cos(x)
y_2 = (x**2)*(np.sin(x)**2)
y_3 = np.log(2*x)

fig, ax = plt.subplots(figsize=(8, 6))

ax.set_title("Графики из задания № 7", fontsize=16)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)

ax.grid(which="major", linewidth=1.2)
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)

ax.plot(x, y_1, c="red", label="(x^2)*cos(x)")
ax.plot(x, y_2, c="blue", label="(x^2)*(sin(x)^2)")
ax.plot(x, y_3, c="green", label="ln(2x)")
ax.legend()

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)

fig.subplots_adjust()

plt.show()
plt.close()