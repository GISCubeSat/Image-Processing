import os
import numpy as np
import matplotlib.pyplot as plt

directory = "LEO"
files = os.listdir(directory)
file_count = len(files)

file_download = open("graph_data.satdata", 'r')

x_vals = []
y_vals = []

for i in range(file_count):
    x_input, y_input = map(float, file_download.readline().split())
    x_vals.append(x_input)
    y_vals.append(y_input)

x = np.array(x_vals)
y = np.array(y_vals)

plt.plot(x, y, 'o')
plt.show()
