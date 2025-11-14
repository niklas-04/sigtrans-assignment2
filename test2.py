import numpy as np
import matplotlib.pyplot as plt

# ======================
# Data för x(t) (sågtand)
# ======================

T0 = 5e-3                      # period [s]
w0 = 2 * np.pi / T0            # grundfrekvens ω0 = 400π rad/s

# Välj N så att |n ω0| ≤ 15e3 rad/s
N = int(15e3 // w0)            # ger N = 11
n = np.arange(-N, N + 1)
wn = n * w0                    # frekvensvektorn ω_n = n ω0

# Fouriertransformen vid dessa frekvenser:
# X(nω0) = 2 j (-1)^n / n, n ≠ 0, och X(0) = 0
Xn = np.zeros_like(wn, dtype=complex)
mask = n != 0
sign = np.where(n[mask] % 2 == 0, 1, -1)   # (-1)^n
Xn[mask] = 2j * sign / n[mask]            # Xn för n ≠ 0

# ======================
# Task 3a: H(ω) och Y(ω)
# ======================

alpha = 1000 * np.pi
Hn = alpha**2 / (alpha + 1j * wn)**2      # H(ω) = α² / (α + jω)²
Yn = Hn * Xn                              # Y(ω) = H(ω) X(ω)

# ======================
# Plotta |X|, |Y| och faser
# ======================

fig, ax = plt.subplots(2, 1, figsize=(9, 6))

# Magnitud
ax[0].stem(wn, np.abs(Xn), label='|X(ω)|')
ax[0].stem(wn, np.abs(Yn), markerfmt='x', label='|Y(ω)|')
ax[0].set_ylabel('Magnitude')
ax[0].set_xlabel('ω [rad/s]')
ax[0].legend()
ax[0].grid(True)

# Fas
ax[1].stem(wn, np.angle(Xn), label='∠X(ω)')
ax[1].stem(wn, np.angle(Yn), markerfmt='x', label='∠Y(ω)')
ax[1].set_ylabel('Phase [rad]')
ax[1].set_xlabel('ω [rad/s]')
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.show()

 