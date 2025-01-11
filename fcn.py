import numpy as np
import matplotlib.pyplot as plt

#Parameters
samp_rate = 32000
freq = 1000
n_samples = round(samp_rate/freq)

#Generate a Hamming window in the time domain

time_window = np.hamming(n_samples)

#compute the frequency response using FFT
freq_response = np.fft.fft(time_window)
freq_magnitude = np.abs(freq_response)
freq_magnitude = freq_magnitude[:n_samples //2] #keep only positive frequencies

#Frequency axis in Hz
freqs = np.fft.fftfreq(n_samples,d=1/samp_rate)[:n_samples // 2]

#plot
plt.figure(figsize=(10,5))

#time domain window
plt.subplot(1,2,1)
plt.plot(time_window)
plt.title("Time Domain - Hamming Window")
plt.xlabel("Samples")
plt.ylabel("Amplitude")

#Frequency domain response
plt.subplot(1,2,2)
plt.plot(freqs,20*np.log10(freq_magnitude))
plt.title("Frequency Domain - Hamming Window")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid()

plt.tight_layout()
plt.show()