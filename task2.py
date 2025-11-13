
import numpy as np
import matplotlib.pyplot as plt

alpha = 1000 * np.pi
omegaZero = 2 * np.pi / 0.005
end = 15 * 10**3
start = -15 * 10**3

omegaN = np.arange(start, end, omegaZero)


Xn = np.array([])

for i in range(len(omegaN)):
    Xn = np.append(Xn, alpha**2 / (alpha + 1j * omegaN[i])**2)

fig , ax = plt.subplots(2 ,1)
ax[0].stem(omegaN, np.abs(Xn))
ax[1].stem(omegaN, np.angle(Xn))

plt.show()