import numpy as np
import matplotlib.pyplot as plt

# ----------------- Global parameters -----------------
T0 = 0.005                      # period
omega0 = 2 * np.pi / T0         # fundamental frequency

# We need at least N = 20 harmonics for part 3b:
Nmax = 40                       # max harmonic index we will store
n = np.arange(-Nmax, Nmax + 1)  # harmonic indices
wn = n * omega0                 # actual frequencies

# ----------------- Spectra Xn, Hn, Yn -----------------
def compute_Y_and_X():
    alpha = 1000 * np.pi

    # Xn (Fourier-series coefficients of X(ω) / (2π))
    Xn = np.zeros_like(n, dtype=complex)
    for k, nk in enumerate(n):
        if nk != 0:
            # your formula: 2π j (-1)^n / (π n)
            Xn[k] = 2 * np.pi * 1j * ((-1.0) ** nk) / (np.pi * nk)
        else:
            Xn[k] = 0.0

    # H(ω) sampled at ω = n ω0
    Hn = np.zeros_like(n, dtype=complex)
    for k, w in enumerate(wn):
        Hn[k] = alpha**2 / (alpha + 1j * w)**2

    Yn = Xn * Hn
    return Yn, Xn

# ----------------- Part 3(b): y(t) for N = 1,2,10,20 -----------------
def part_b():
    Yn, _ = compute_Y_and_X()

    # time vector: 0 < t < 15 ms
    dt = 1e-5                     # time step (10 µs, fine enough)
    t = np.arange(0, 15e-3, dt)

    Ns = [1, 2, 10, 20]

    fig, ax = plt.subplots()
    for N in Ns:
        y_t = np.zeros_like(t, dtype=complex)

        # y(t) ≈ 1/(2π) Σ_{|n|≤N} Y(nω0) e^{j n ω0 t}
        for ti, tt in enumerate(t):
            s = 0.0 + 0.0j
            for k, nk in enumerate(n):
                if abs(nk) <= N:
                    s += Yn[k] * np.exp(1j * nk * omega0 * tt)
            y_t[ti] = (1 / (2 * np.pi)) * s

        # remove tiny imaginary parts from numerical error
        y_t = np.real_if_close(y_t, tol=1e-12)

        ax.plot(t, y_t, label=f'N = {N}')

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("y(t)")
    ax.set_xlim(0, 15e-3)
    ax.legend()
    ax.grid(True)
    ax.set_title("Output signal y(t) for different N (Task 3b)")
    plt.show()

    return t, y_t

# ----------------- Optional: spectra plot X(ω), Y(ω) -----------------
def plot_spectra():
    Yn, Xn = compute_Y_and_X()

    fig, ax = plt.subplots(2, 1, figsize=(9, 6))

    # Magnitude
    ax[0].stem(wn, np.abs(Xn), label='|X(ω)|', use_line_collection=True)
    ax[0].stem(wn, np.abs(Yn), markerfmt='x', label='|Y(ω)|',
               use_line_collection=True)
    ax[0].set_ylabel('Magnitude')
    ax[0].set_xlabel('ω [rad/s]')
    ax[0].legend()
    ax[0].grid(True)

    # Phase
    ax[1].stem(wn, np.angle(Xn), label='∠X(ω)', use_line_collection=True)
    ax[1].stem(wn, np.angle(Yn), markerfmt='x', label='∠Y(ω)',
               use_line_collection=True)
    ax[1].set_ylabel('Phase [rad]')
    ax[1].set_xlabel('ω [rad/s]')
    ax[1].legend()
    ax[1].grid(True)

    plt.tight_layout()
    plt.show()

# ---- run part 3(b) ----
t, y_t = part_b()

# ---- if you also want the spectra plot, call: ----
# plot_spectra()
