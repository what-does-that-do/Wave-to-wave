import numpy as np#
import wave
from matplotlib import pyplot as plt

LOWEST_HZ = 20
HIGHEST_HZ = 300
CHUNKS = 5000

f = wave.open("test.wav", "rb")

print("Sample frequency = ", f.getframerate())
print("Total number of frames = ", f.getnframes())
print("Framerate = ", f.getframerate())
print("This file has",f.getnchannels(),"channels!")
sample_width = f.getsampwidth()
print("Wizard 🧙‍♂️ says bit depth =", sample_width)

sampleWidth = f.getframerate()
all_frames = f.readframes(f.getnframes())

last_value = 0

last_value += CHUNKS
if len(all_frames) > last_value:
    CHUNKS = len(all_frames) - last_value
    last_value = len(all_frames)

frames = []
initial_value = last_value - CHUNKS
for i in range(CHUNKS):
    frames.append(all_frames[initial_value + i])

print(len(frames))

amplitudes = []

# Trial and errors each frequency
for frequency in range(LOWEST_HZ, HIGHEST_HZ):
    print("Checking",frequency,"hz...", end='\r')
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

# if there are bit depth is 2, we need to scale the frequencies to match the fact that we have 2 frames (channels) in each frame.
start_hz = LOWEST_HZ * sample_width
end_hz = HIGHEST_HZ * sample_width

# plot on a graph against frequencies.
# x = frequency range multiplied by bit depth, because if there are 2 bits per sample frequencies are halved...
# y = amplitude for that frequency. If the frequency is around 0, it's not in the wav file.
plt.plot(range(start_hz, end_hz, sample_width), amplitudes)
plt.savefig("amps.jpg")

found_frequencies = []
for i in range(len(amplitudes)):
    if amplitudes[i] > 50: # a rough place on the graph that usually is accurate
        frequency = start_hz + i*sample_width
        found_frequencies.append(frequency)

print("Found frequencies:", found_frequencies)
print("\n🧙‍♂️ Finished!!")