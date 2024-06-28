import numpy as np#
import wave
from matplotlib import pyplot as plt

f = wave.open("test.wav", "rb")

print("Sample frequency = ", f.getframerate())
print("Total number of frames = ", f.getnframes())
print("Framerate = ", f.getframerate())
print("This file has",f.getnchannels(),"channels!")
sample_width = f.getsampwidth()
print("Wizard 🧙‍♂️ says bit depth =", sample_width)

sampleWidth = f.getframerate()
frames = f.readframes(6000)
amplitudes = []

# Trial and errors each frequency
for frequency in range(20, 300):
    print("Checking",frequency,"hz (max 300)", end='\r')
    xcords = 0
    ycords = 0

    #for each frame in the wav file, test if it could be that frequency
    for i in range(len(frames)):
        angle = (i / sampleWidth * frequency * np.pi * 2) # finding angle between the y and the x axis
        # find x and y co-ords, using sochatoa find the amplitude
        xcords += np.cos(angle) * frames[i]
        ycords += np.sin(angle) * frames[i]
    # find the average amplitude
    averagex = xcords / sampleWidth
    averagey = ycords / sampleWidth
    averageAmplitude = (averagex * averagex) + (averagey * averagey)
    # add this amplitude to our list, to be analysed later.
    amplitudes.append(averageAmplitude)

# plot on a graph against frequencies.
# x = frequency range multiplied by bit depth, because if there are 2 bits per sample frequencies are halved...
# y = amplitude for that frequency. If the frequency is around 0, it's not in the wav file.
plt.plot(range(20*sample_width, 300*sample_width, sample_width), amplitudes)
plt.savefig("amps.jpg")

found_frequencies = []
for i in range(len(amplitudes)):
    if amplitudes[i] > 50: # a rough place on the graph that usually is accurate
        frequency = (20 * sample_width) + (i * sample_width)
        found_frequencies.append(frequency)

print("Found frequencies:", found_frequencies)
print("\n🧙‍♂️ Finished!!")