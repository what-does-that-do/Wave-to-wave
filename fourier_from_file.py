import numpy as np

f = 3.0
t = np.arange(0,2,0.001)

cos_wave = np.cos(2*np.pi*f*t)

r_cord = []
min_freq_range = 0.0
max_freq_range = 10.0

sf_list = np.arange(min_freq_range, max_freq_range, 0.1)
for sf in sf_list:
    r_cord.append( [(cos_wave[i], t[i]*sf*2*np.pi) for i in range(len(t))] )

x_cord , y_cord = [], []
for l in range(len(r_cord)):
    x_cord.append( [amp*np.cos(theta) for (amp,theta) in r_cord[l]] )
    y_cord.append( [amp*np.sin(theta) for (amp,theta) in r_cord[l]] )

mean_list = []

for l in range(len(r_cord)):
    # Storing the COM for plotting later
    x_mean = np.sum(x_cord[l])
    mean_list.append(x_mean)

print(sf_list[np.where(mean_list == np.max(mean_list))][0])