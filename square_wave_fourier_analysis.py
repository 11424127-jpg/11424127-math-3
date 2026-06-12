
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# --- Problem 1: Square Wave Signal Analysis ---

def square_wave(t, T, V_oh, V_ol, duty_cycle):
    period_t = t % T
    if 0 <= period_t < T * duty_cycle:
        return V_oh
    else:
        return V_ol

def fourier_series_coefficients(T, V_oh, V_ol, duty_cycle, N_terms):
    omega0 = 2 * np.pi / T

    # Calculate a0
    a0_integrand = lambda t: square_wave(t, T, V_oh, V_ol, duty_cycle)
    a0 = (1/T) * quad(a0_integrand, 0, T)[0]

    an_coeffs = []
    bn_coeffs = []

    for n in range(1, N_terms + 1):
        an_integrand = lambda t: square_wave(t, T, V_oh, V_ol, duty_cycle) * np.cos(n * omega0 * t)
        bn_integrand = lambda t: square_wave(t, T, V_oh, V_ol, duty_cycle) * np.sin(n * omega0 * t)
        
        an = (2/T) * quad(an_integrand, 0, T)[0]
        bn = (2/T) * quad(bn_integrand, 0, T)[0]
        
        an_coeffs.append(an)
        bn_coeffs.append(bn)
        
    return a0, an_coeffs, bn_coeffs

def reconstruct_square_wave(t_values, T, a0, an_coeffs, bn_coeffs, N_terms):
    omega0 = 2 * np.pi / T
    reconstructed_signal = np.full_like(t_values, a0)

    for n in range(N_terms):
        reconstructed_signal += an_coeffs[n] * np.cos((n + 1) * omega0 * t_values) + \
                                bn_coeffs[n] * np.sin((n + 1) * omega0 * t_values)
    return reconstructed_signal

# Parameters for Problem 1
T_ns = 10 # ns
T = T_ns * 1e-9 # seconds
f = 1 / T # Hz (100 MHz)
V_oh = 3.3 # Volts
V_ol = 0 # Volts
duty_cycle = 0.5 # 50%
N_terms = 50 # Number of Fourier terms for approximation

# Calculate Fourier coefficients
a0, an_coeffs, bn_coeffs = fourier_series_coefficients(T, V_oh, V_ol, duty_cycle, N_terms)

# Time values for plotting
t_values = np.linspace(0, 3 * T, 500)

# Original square wave values
original_wave = np.array([square_wave(t, T, V_oh, V_ol, duty_cycle) for t in t_values])

# Reconstruct square wave
reconstructed_wave = reconstruct_square_wave(t_values, T, a0, an_coeffs, bn_coeffs, N_terms)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(t_values * 1e9, original_wave, label='Original Square Wave', linestyle='--')
plt.plot(t_values * 1e9, reconstructed_wave, label=f'Fourier Series Approximation ({N_terms} terms)')
plt.title('Square Wave Fourier Series Approximation')
plt.xlabel('Time (ns)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend()
plt.savefig('square_wave_fourier_approximation.png')
plt.close()

# Frequency Spectrum Analysis
frequencies = np.array([(n + 1) * f for n in range(N_terms)])
amplitudes = np.sqrt(np.array(an_coeffs)**2 + np.array(bn_coeffs)**2)

plt.figure(figsize=(12, 6))
plt.stem(frequencies / 1e6, amplitudes, basefmt='b-')
plt.title('Frequency Spectrum of Square Wave')
plt.xlabel('Frequency (MHz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.savefig('square_wave_frequency_spectrum.png')
plt.close()

print("Square wave Fourier analysis completed. Plots saved as 'square_wave_fourier_approximation.png' and 'square_wave_frequency_spectrum.png'.")

# Explanation for trailing edge distortion (This part will be in the README or a separate text file)
# The trailing edge distortion (ringing or overshoot/undershoot) in a square wave transmitted through a long conductor is primarily due to the limited bandwidth of the transmission medium and the presence of higher-order harmonics in the square wave. A perfect square wave contains an infinite number of odd harmonics. When transmitted through a real-world conductor, which acts as a low-pass filter, these higher-frequency components are attenuated or phase-shifted differently. This causes the sharp edges of the square wave to become rounded, and the interaction between the remaining harmonics can lead to ringing effects at the transitions. This phenomenon is known as the Gibbs phenomenon in Fourier series approximation, where truncating the series (or filtering out high frequencies) leads to oscillations near discontinuities. Additionally, impedance mismatches and reflections on the transmission line can also contribute to signal integrity issues, including distortion and ringing.
