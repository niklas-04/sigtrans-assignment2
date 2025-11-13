
import numpy as np
import matplotlib.pyplot as plt

omegaZero = 2 * np.pi / 0.005
N = 15 * 10**3 / omegaZero

omegaN = np.arange(-N, N+1, 1) * omegaZero

Xn = np.array([])

for i in range(len(omegaN)):
    Xn = np.append(Xn, 2 * np.pi * 1j * (-1**omegaN[i]) / (np.pi * omegaN[i]))
fig , ax = plt.subplots(2 ,1)
ax[0].stem(omegaN, np.abs(Xn))
ax[1].stem(omegaN, np.angle(Xn))

plt.show()