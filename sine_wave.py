import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/algez/Downloads/design_project/sine_voltages.csv")
sine_values_voltage = df['values'].values.tolist()

sine_values_voltage2 = [2.51, 3.27, 3.98, 4.53, 4.88, 5.0, 4.88, 4.53, 3.98, 3.27, 2.51, 1.75, 1.04, 0.49, 0.14, 0.02, 0.14, 0.49, 1.04, 1.75, 2.51]

if(sine_values_voltage == sine_values_voltage2):
    print(True)

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
