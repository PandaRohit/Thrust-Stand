import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load data
data = pd.read_csv('TTS.csv')

fig, ax = plt.subplots(5, sharex=True)
fig.subplots_adjust(hspace=0.75)
x = data['Time']

ax[0].plot(x, data['Voltage (V)'])
ax[0].set_title('Voltage')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('V')
ax[0].set_yticks(np.arange(min(data['Voltage (V)'])*0.1, max(data['Voltage (V)'])+0.1, (max(data['Voltage (V)'])-min(data['Voltage (V)'])+0.2)/5))

ax[1].plot(x, data['Current (A)'])
ax[1].set_title('Current')
ax[1].set_ylabel('A')
ax[1].set_yticks(np.arange(min(data['Current (A)'])-0.1, max(data['Current (A)'])+0.1, (max(data['Current (A)'])-min(data['Current (A)'])+0.2)/5))

ax[2].plot(x, data['Thrust Force (g)'])
ax[2].set_title('Thrust Force')
ax[2].set_ylabel('g')
ax[2].set_yticks(np.arange(min(data['Thrust Force (g)'])-0.1, max(data['Thrust Force (g)'])+0.1, (max(data['Thrust Force (g)'])-min(data['Thrust Force (g)'])+0.2)/5))
print(np.arange(min(data['Thrust Force (g)'])-0.1, max(data['Thrust Force (g)'])+0.1, (max(data['Thrust Force (g)'])-min(data['Thrust Force (g)'])+0.2)/5))
print(max(data['Thrust Force (g)'])+0.1)

ax[3].plot(x, data['Temperature (C)'])
ax[3].set_title('Temperature')
ax[3].set_ylabel('C')
ax[3].set_yticks(np.arange(min(data['Temperature (C)'])-0.1, max(data['Temperature (C)'])+0.1, (max(data['Temperature (C)'])-min(data['Temperature (C)'])+0.2)/5))

ax[4].plot(x, data['Speed (RPM)'])
ax[4].set_title('Speed')
ax[4].set_ylabel('RPM')
ax[4].set_yticks(np.arange(min(data['Speed (RPM)'])-0.1, max(data['Speed (RPM)'])+0.1, (max(data['Speed (RPM)'])-min(data['Speed (RPM)'])+0.2)/5))

fig.suptitle('TTS data graphs', fontsize=16)

plt.show()
