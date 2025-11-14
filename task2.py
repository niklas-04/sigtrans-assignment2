
import numpy as np
import matplotlib.pyplot as plt

alpha = 1000 * np.pi
end = 15 * 10**3
start = -15 * 10**3
timeStep = 1

omegaN = np.arange(start, end, timeStep)


Hn = np.array([])

for i in range(len(omegaN)):
    Hn = np.append(Hn, alpha**2 / (alpha + 1j * omegaN[i])**2)

fig , ax = plt.subplots(2 ,1)
ax[0].plot(omegaN, np.abs(Hn))
ax[1].plot(omegaN, np.angle(Hn))

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