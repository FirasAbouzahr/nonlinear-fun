# Firas Abouzahr
# Feb 4th 2024

import numpy as np
import matplotlib.pyplot as plt

def logmap(x,r):
    return r * x * (1 - x)

### plot x_n as a function of n ###

N = 100
r = 4
x0 = .212

xvals = [x0]

for n in range(N-1):
    x_n = logmap(x0,r)
    xvals.append(x_n)
    x0 = x_n

# as a function of n
plt.plot(range(N),xvals)
plt.title("r = {}".format(r),fontsize = 14)
plt.xlabel("Time [n]",fontsize = 14)
plt.ylabel(r"$x_n$",fontsize = 14)
plt.show()


### plot x_n as a function of r ###

R = np.linspace(3,4,300)
x_0 = 0.5

xvals_r = []

for r in R:
    x_n = logmap(x0,r)
    xvals_r.append(x_n)
    x0 = x_n

# as a function of r
plt.plot(R,xvals_r)
plt.xlabel("r",fontsize = 14)
plt.ylabel(r"$x_{n}$",fontsize = 14)
plt.show()

