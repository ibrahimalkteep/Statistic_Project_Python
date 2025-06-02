import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline

class_intervals = ['55 - 60', '60 - 65', '65 - 70', '70 - 75', '75 - 80', '80 - 85', '85 - 90', '90 - 95']
frequencies = [8, 10, 15, 20, 12, 8, 4, 2]
lower_bounds = [int(i.split('-')[0]) for i in class_intervals]
upper_bounds = [int(i.split('-')[1]) for i in class_intervals]
midpoints = [(low + high) / 2 for low, high in zip(lower_bounds, upper_bounds)]

modified_cf = [frequencies[0]] + [frequencies[i] + frequencies[i-1] for i in range(1, len(frequencies))]

df = pd.DataFrame({
    'Class Interval': class_intervals,
    'Midpoint': midpoints,
    'Frequency': frequencies,
    'C.F': modified_cf
})

fig, axs = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Statistical Charts', fontsize=16)

axs[0, 0].bar(class_intervals, frequencies, color='skyblue', edgecolor='black')
for i, val in enumerate(frequencies):
    axs[0, 0].text(i, val + 0.5, str(val), ha='center')
axs[0, 0].set_title("Histogram")
axs[0, 0].set_xlabel("Class of degree")
axs[0, 0].set_ylabel("Frequency")

extended_midpoints = [midpoints[0] - 5] + midpoints + [midpoints[-1] + 5]
extended_frequencies = [0] + frequencies + [0]
axs[0, 1].plot(extended_midpoints, extended_frequencies, marker='o', color='darkblue')
axs[0, 1].set_title("Frequency Polygon")
axs[0, 1].set_xlabel("Midpoint")
axs[0, 1].set_ylabel("Frequency")

x_new = np.linspace(min(midpoints), max(midpoints), 300)
spl = make_interp_spline(midpoints, frequencies, k=3)
y_smooth = spl(x_new)
axs[0, 2].plot(x_new, y_smooth, color='teal')
axs[0, 2].set_title("Frequency Curve")
axs[0, 2].set_xlabel("Class of degree")
axs[0, 2].set_ylabel("Frequency")

axs[1, 0].plot(midpoints, frequencies, label="Frequency", marker='o')
axs[1, 0].plot(midpoints, modified_cf, label="C.F", color='orangered')
axs[1, 0].set_title("Frequency Ogive")
axs[1, 0].legend()

table_text = df.to_string(index=False)
axs[1, 1].axis('off')
axs[1, 1].text(0, 0.6, table_text, fontfamily='monospace', fontsize=10, verticalalignment='top')


axs[1, 2].axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
