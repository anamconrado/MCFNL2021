import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 500e-6, 1001)
s0 = 10e-6
t0 = s0 * 10
y = np.exp(-np.power(t-t0, 2)/(s0**2))

y_fft = np.fft.fft(y)

plt.plot(t, y_fft)
plt.show()
