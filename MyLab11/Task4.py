import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)

#Task1
x = np.linspace(-10, 10, 100)
y_1 = (x**2)*np.cos(x)
y_2 = (x**2)*(np.sin(x)**2)
y_3 = np.log(2*x)

fig_1, ax_1 = plt.subplots(3, 1)
ax_1[0].plot(x, y_1, c="red", label="(x^2)*cos(x)")
ax_1[1].plot(x, y_2, c="blue", label="(x^2)*(sin(x)^2)")
ax_1[2].plot(x, y_3, c="green", label="ln(2x)")

for i in range(0, 3):
    ax_1[i].set_xlabel("x", fontsize=14)
    ax_1[i].set_ylabel("y", fontsize=14)

    ax_1[i].grid(which="major", linewidth=1.2)
    ax_1[i].grid(which="minor", linestyle="--", color="gray", linewidth=0.5)

    ax_1[i].xaxis.set_minor_locator(AutoMinorLocator())
    ax_1[i].yaxis.set_minor_locator(AutoMinorLocator())

    ax_1[i].tick_params(which='major', length=10, width=2)
    ax_1[i].tick_params(which='minor', length=5, width=1)

    ax_1[i].legend()

fig_1.subplots_adjust(hspace=0.5)
fig_1.savefig('Графики 1.png', dpi = 300)

plt.show()
plt.close()

#Task11
x = np.linspace(-10, 10, 100)

y_1 = np.log(2*x)/np.log(1)
y_2 = np.log2(2*x)
y_3 = np.log(2*x)/np.log(3)
y_4 = np.log(2*x)/np.log(6)

fig_2, ax_2 = plt.subplots(4, 1)

ax_2[0].plot(x, y_1, c="red", label="log1(2x)")
ax_2[1].plot(x, y_2, c="blue", label="log2(2x)")
ax_2[2].plot(x, y_3, c="green", label="log4(2x)")
ax_2[3].plot(x, y_4, c="black", label="log6(2x)")

for i in range(0, 4):
    ax_2[i].set_xlabel("x", fontsize=14)
    ax_2[i].set_ylabel("y", fontsize=14)

    ax_2[i].grid(which="major", linewidth=1.2)
    ax_2[i].grid(which="minor", linestyle="--", color="gray", linewidth=0.5)

    ax_2[i].xaxis.set_minor_locator(AutoMinorLocator())
    ax_2[i].yaxis.set_minor_locator(AutoMinorLocator())

    ax_2[i].tick_params(which='major', length=10, width=2)
    ax_2[i].tick_params(which='minor', length=5, width=1)

    ax_2[i].legend()

fig_2.subplots_adjust(hspace=0.5)
fig_2.savefig('Графики 2.png', dpi = 400)

plt.show()
plt.close()

#Task2
data1 = pd.read_csv('Sigma.csv', delimiter=';')
r = data1['r']
y = data1['Sigma']

data2 = np.loadtxt('lambda.csv', delimiter= ';', skiprows= 1)
rr = data2[:, 0]
yy = data2[:, 1]

data3 = pd.read_csv('Vfi.csv', delimiter=';')
rrr = data3['r']
yyy = data3['Vfi']

fig_3, ax_3 = plt.subplots(3, 1)
ax_3[0].plot(r, y, c="red", label="Sigma(r)")
ax_3[1].plot(rr, yy, 'b--', label="Lambda(r)")
ax_3[2].plot(rrr, yyy, c="green", label="Vfi(r)")

for i in range(0, 3):
    ax_3[i].set_xlabel("x", fontsize=14)
    ax_3[i].set_ylabel("y", fontsize=14)

    ax_3[i].grid(which="major", linewidth=1.2)
    ax_3[i].grid(which="minor", linestyle="--", color="gray", linewidth=0.5)

    ax_3[i].xaxis.set_minor_locator(AutoMinorLocator())
    ax_3[i].yaxis.set_minor_locator(AutoMinorLocator())

    ax_3[i].tick_params(which='major', length=10, width=2)
    ax_3[i].tick_params(which='minor', length=5, width=1)

    ax_3[i].legend()

fig_3.subplots_adjust(hspace=0.7)
fig_3.savefig('Графики 3.png', dpi = 500)
plt.show()
plt.close()