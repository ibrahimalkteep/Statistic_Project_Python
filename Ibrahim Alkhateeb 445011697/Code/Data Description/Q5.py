import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline

class_intervals = ['20 - 30', '30 - 40', '40 - 50', '50 - 60', '60 - 70', '70 - 80', '80 - 90']  # class intervals
frequencies = [8, 12, 25, 32, 22, 18, 5]
lower_bounds = [int(i.split('-')[0]) for i in class_intervals]
upper_bounds = [int(i.split('-')[1]) for i in class_intervals]
midpoints = [(low + high) / 2 for low, high in zip(lower_bounds, upper_bounds)]



df = pd.DataFrame({
    'Class Interval': class_intervals,
    'Midpoint': midpoints,
    'Frequency': frequencies,
    'relative Frequency': [f / sum(frequencies) for f in frequencies],
    'relative frequency (%)': [f / sum(frequencies) * 100 for f in frequencies],
})

fig, axs = plt.subplots(2, 2, figsize=(18, 10))
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
axs[1, 0].plot(x_new, y_smooth, color='teal')
axs[1, 0].set_title("Frequency Curve")
axs[1, 0].set_xlabel("Class of degree")
axs[1, 0].set_ylabel("Frequency")


table_text = df.to_string(index=False)
axs[1, 1].axis('off')
axs[1, 1].text(0, 0.6, table_text, fontfamily='monospace', fontsize=10, verticalalignment='top')




plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
