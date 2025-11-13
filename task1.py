import numpy as np
import matplotlib.pyplot as plt

omegaZero = 2 * np.pi / 0.005
start = -15 * 10**3
end = 15 * 10**3
N = end / omegaZero

omegaN = np.arange(-N, N+1, 1) * omegaZero
Xn = np.zeros_like(omegaN)

for i in range(len(omegaN)):
    Xn[i] = 2 * np.pi * (-1**omegaN[i]) / (np.pi * omegaN[i])

fig , ax = plt.subplots(2 ,1)
ax[0].stem(omegaN, np.abs(Xn))
ax[1].stem(omegaN, np.angle(Xn))

plt.show()