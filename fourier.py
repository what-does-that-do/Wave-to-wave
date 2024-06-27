import numpy as np
import wave

f = 3.0
t = np.arange(0,2,0.001)

f = wave.open("test.wav", "rb")

print("Sample frequency = ", f.getframerate())
print("Total number of frames = ", f.getnframes())
print("Framerate = ", f.getframerate())

print("Getting 1/8 second's worth of frames (", int(f.getframerate()/8), ") frames...")

frames = f.readframes(f.getframerate())
pcm_samples = np.frombuffer(frames, dtype="<h")
normalized_amplitudes = pcm_samples / (2 ** 15)

r_cord = []
min_freq_range = 20.0
max_freq_range = f.getframerate() / 2 # nyquist

cos_wave = normalized_amplitudes

print("Adding to r_cord...")
sf_list = np.arange(min_freq_range, max_freq_range, 0.1)
for sf in sf_list:
    r_cord.append( [(cos_wave[i], t[i]*sf*2*np.pi) for i in range(len(t))] )
print("Sorting out x and y...")
x_cord , y_cord = [], []
for l in range(len(r_cord)):
    x_cord.append( [amp*np.cos(theta) for (amp,theta) in r_cord[l]] )
    y_cord.append( [amp*np.sin(theta) for (amp,theta) in r_cord[l]] )

mean_list = []

print("Calculating COM...")
for l in range(len(r_cord)):
    # Storing the COM for plotting later
    x_mean = np.sum(x_cord[l])
    mean_list.append(x_mean)

print(sf_list[np.where(mean_list == np.max(mean_list))][0])