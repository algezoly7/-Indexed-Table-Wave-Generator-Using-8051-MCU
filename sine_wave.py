import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/algez/Downloads/design_project/sine_voltages.csv")
sine_values_voltage = df['values'].values.tolist()

sample_period_us = 20
time_points_us = [i * sample_period_us for i in range(len(sine_values_voltage))]

plt.figure(figsize=(10, 6))
plt.plot(time_points_us, sine_values_voltage, linestyle='-', drawstyle='steps-pre')
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.grid(True)
plt.xticks(np.arange(0, max(time_points_us) + 1, 100))
plt.yticks(np.arange(-2, 7, 0.5))
plt.ylim(-2, 7)
plt.show()
