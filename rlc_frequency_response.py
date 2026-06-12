
import numpy as np
import matplotlib.pyplot as plt

# --- Problem 2: RLC Circuit Frequency Response ---

def rlc_bandpass_filter_response(R, L, C, frequencies):
    omega = 2 * np.pi * frequencies
    
    # Impedance of inductor and capacitor
    ZL = 1j * omega * L
    ZC = 1 / (1j * omega * C)
    
    # Total impedance of the series RLC circuit
    Z_total = R + ZL + ZC
    
    # Transfer function (Output voltage across capacitor / Input voltage)
    # Vo/Vi = Zc / Z_total
    transfer_function = ZC / Z_total
    
    return transfer_function

# Parameters for Problem 2
R = 10 # Ohms
L = 1e-3 # Henry (1 mH)
C = 2.53e-8 # Farad (2.53 * 10^-8 F)

# Frequencies for plotting
frequencies = np.logspace(4, 8, 500) # From 10 kHz to 100 MHz

# Calculate transfer function
tf = rlc_bandpass_filter_response(R, L, C, frequencies)

# Magnitude and Phase
magnitude = np.abs(tf)
phase = np.angle(tf, deg=True)

# Plotting Magnitude Response
plt.figure(figsize=(12, 6))
plt.semilogx(frequencies, 20 * np.log10(magnitude))
plt.title("RLC Bandpass Filter Magnitude Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(True, which="both", ls="-")
plt.savefig("rlc_magnitude_response.png")
plt.close()

# Plotting Phase Response
plt.figure(figsize=(12, 6))
plt.semilogx(frequencies, phase)
plt.title("RLC Bandpass Filter Phase Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")
plt.grid(True, which="both", ls="-")
plt.savefig("rlc_phase_response.png")
plt.close()

print("RLC circuit frequency response analysis completed. Plots saved as 'rlc_magnitude_response.png' and 'rlc_phase_response.png'.")
