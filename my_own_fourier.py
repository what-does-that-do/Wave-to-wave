import numpy as np#
import wave
from matplotlib import pyplot as plt

f = wave.open("test.wav", "rb")

print("Sample frequency = ", f.getframerate())
print("Total number of frames = ", f.getnframes())
print("Framerate = ", f.getframerate())

sampleWidth = f.getframerate()
frames = f.readframes(1000)

pcm_samples = np.frombuffer(frames, dtype="<h")
normalised_amplitides = np.int16((pcm_samples / pcm_samples.max()) * 32767)
amplitudes = []

for frequency in range(20, 300):
    xcords = 0
    ycords = 0

    #for sample in normalised_amplitides:
        
    for i in range(len(normalised_amplitides)):
        angle = (i / sampleWidth * frequency * np.pi * 2) # finding angle between the y and the x axis
        xcords += np.cos(angle) * normalised_amplitides[i]
        ycords += np.sin(angle) * normalised_amplitides[i]
    
    averagex = xcords / sampleWidth
    averagey = ycords / sampleWidth
    averageAmplitude = (averagex * averagex) + (averagey * averagey)

    amplitudes.append(averageAmplitude)

plt.plot(amplitudes)
plt.savefig("amps.jpg")