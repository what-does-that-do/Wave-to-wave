from scipy.fft import fft, fftfreq
import wave
import numpy as np
from matplotlib import pyplot as plt

f = wave.open("test.wav", "rb")

print("Sample frequency = ", f.getframerate())
print("Total number of frames = ", f.getnframes())
print("Framerate = ", f.getframerate())

frames = f.readframes(f.getframerate())
pcm_samples = np.frombuffer(frames, dtype="<h")
normalised_amplitides = np.int16((pcm_samples / pcm_samples.max()) * 32767)

plt.plot(normalised_amplitides[:1000])
plt.savefig("norm_amplitudes.jpg")

min_freq_range = 20.0
max_freq_range = f.getframerate() / 2 # nyquist

N = f.getnframes()

yf = fft(normalised_amplitides)
xf = fftfreq(N, 1 / f.getframerate())

plt.plot(np.abs(yf))
plt.savefig("yf.jpg")

plt.plot(np.abs(xf))
plt.savefig("xf.jpg")