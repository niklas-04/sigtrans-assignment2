import numpy as np
import matplotlib.pyplot as plt

omegaZero = 2 * np.pi / 0.005
N = int(np.floor(15 * 10**3 / omegaZero))

omegaN = np.arange(-N, N+1)

Xn = np.array([])

for i in range(len(omegaN)):
    if omegaN[i] != 0:
        Xn = np.append(Xn, 2 * np.pi * 1j * ((-1.0)**omegaN[i]) / (np.pi * omegaN[i]))
    else:
        Xn = np.append(Xn, 0)
    

fig , ax = plt.subplots(2 ,1)
ax[0].stem(omegaN, np.abs(Xn))
ax[1].stem(omegaN, np.angle(Xn))

ax[0].set_title("Magnitude spectrum |X(ω)|")
ax[0].set_xlabel(r'$\omega$ [rad/s]')
ax[0].set_ylabel('|X(ω)|')
ax[0].grid(True)

ax[1].set_title("Phase spectrum ∠X(ω)")
ax[1].set_xlabel(r'$\omega$ [rad/s]')
ax[1].set_ylabel('Phase [rad]')
ax[1].grid(True)


plt.tight_layout()
plt.show()