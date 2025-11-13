import numpy as np
import matplotlib.pyplot as plt

# Period och grundfrekvens
T0 = 0.005
w0 = 2 * np.pi / T0

# Max frekvens för plot
w_max = 15000

# Antal Fouriertermer
N = int(np.floor(w_max / w0))

# Diskreta n
n = np.arange(-N, N+1)

# Beräkna Fourierkoefficienter C_n
Cn = np.zeros_like(n, dtype=complex)
nonzero = n != 0
Cn[nonzero] = 2j * (-1.0)**n[nonzero] / (5 * n[nonzero] * np.pi)
Cn[n==0] = 0  # C0

# Kontinuerlig Fouriertransform X(ω) vid ω = n*w0
Xn = 2 * np.pi * Cn
wn = n * w0

# Skapa plot
fig, ax = plt.subplots(2, 1, figsize=(10,6))

# Magnitudspektrum
ax[0].stem(wn, np.abs(Xn), basefmt=" ")
ax[0].set_title("Magnitude spectrum |X(ω)|")
ax[0].set_xlabel(r'$\omega$ [rad/s]')
ax[0].set_ylabel('|X(ω)|')
ax[0].grid(True)

# Fasespektrum
ax[1].stem(wn, np.angle(Xn), basefmt=" ")
ax[1].set_title("Phase spectrum ∠X(ω)")
ax[1].set_xlabel(r'$\omega$ [rad/s]')
ax[1].set_ylabel('Phase [rad]')
ax[1].grid(True)

plt.tight_layout()
plt.show()