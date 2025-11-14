import numpy as np
import matplotlib.pyplot as plt

omegaZero = 2 * np.pi / 0.005
N = int(np.floor(15 * 10**3 / omegaZero))
omegaN = np.arange(-N, N+1)
xaxis = omegaN * omegaZero
def Y():
    alpha = 1000 * np.pi
    Xn = np.array([])
    Hn = alpha**2 / (alpha + 1j * omegaZero * omegaN)**2
    for i in range(len(omegaN)):
            if omegaN[i] != 0:
                    Xn = np.append(Xn, 2 * np.pi * 1j * ((-1.0)**omegaN[i]) / (np.pi * omegaN[i]))
            else:
                    Xn = np.append(Xn, 0)

    Yn = Xn * Hn
    return (Yn, Xn)

def part_b():
	N = 20
	y_w, _ = Y()
	y_t = np.array([])
	timeVector = np.arange(0, 15*10**-3, 10**-3)

	for i in range(len(timeVector)):
		sum = 0
		for j in range((2*N)):
			if j == len(y_w)-1:
				break
			else:
				sum += (1/(2 * np.pi)) * y_w[j] * np.exp(1j*timeVector[i]*j*omegaN[j])
		y_t = np.append(y_t, sum)
	fig, ax = plt.subplots()
	ax.plot(timeVector, y_t, label="dirac delta * h (convolution)")
	ax.set_xlabel("Time (s)")
	ax.set_ylabel("y(t)")
	ax.set_xlim(0, 15 * 10**-3)
	ax.legend()
	plt.show()
	return y_t
        
(Yn, Xn) = Y()
fig, ax = plt.subplots(2, 1, figsize=(9, 6))


# Magnitud
ax[0].stem(xaxis, np.abs(Xn), label='|X(ω)|')
ax[0].stem(xaxis, np.abs(Yn), markerfmt='x', label='|Y(ω)|')
ax[0].set_ylabel('Magnitude')
ax[0].set_xlabel('ω [rad/s]')
ax[0].legend()
ax[0].grid(True)

# Fas
ax[1].stem(xaxis, np.angle(Xn), label='∠X(ω)')
ax[1].stem(xaxis, np.angle(Yn), markerfmt='x', label='∠Y(ω)')
ax[1].set_ylabel('Phase [rad]')
ax[1].set_xlabel('ω [rad/s]')
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.show()
