from scipy.fft import fft, ifft
import wave
import numpy as np

f = wave.open("test.wav", "rb")

print("Sample frequency = ", f.getframerate())
print("Total number of frames = ", f.getnframes())
print("Framerate = ", f.getframerate())

print("Getting 1/32 second's worth of frames (", int(f.getframerate()/32), ") frames...")

frames = f.readframes(f.getframerate())
pcm_samples = np.frombuffer(frames, dtype="<h")
normalized_amplitudes = pcm_samples / (2 ** 15)

min_freq_range = 20.0
max_freq_range = f.getframerate() / 2 # nyquist

print(fft(normalized_amplitudes))