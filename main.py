import wave
import numpy as np

f = wave.open("test.wav", "rb")

print("Sample frequency = ", f.getframerate())
print("Total number of frames = ", f.getnframes())
print("Framerate = ", f.getframerate())

print("Getting 1/8 second's worth of frames (", int(f.getframerate()/8), ") frames...")

frames = f.readframes(f.getframerate())
pcm_samples = np.frombuffer(frames, dtype="<h")
normalized_amplitudes = pcm_samples / (2 ** 15)

print(normalized_amplitudes)

csv = open("frames.csv", "w")
for frame in normalized_amplitudes:
    csv.write(str(frame) + "\n")