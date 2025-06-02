import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline


bins = [21, 27.5, 34, 40.5, 47, 53.5, 60]
labels = ["21–27.5", "27.5–34", "34–40.5", "40.5–47", "47–53.5", "53.5–60"]
frequencies = [6, 6, 6, 6, 6, 6]
midpoints = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)]

total = sum(frequencies)
relative_freq = [f / total for f in frequencies]
percent_freq = [rf * 100 for rf in relative_freq]
cumulative_freq = np.cumsum(frequencies)

df = pd.DataFrame({
    "Class Interval": labels,
    "Midpoint": midpoints,
    "Frequency": frequencies,
})
print(df.to_string(index=False))
df2= {
    "Max": 52,
    "Min": 21,
    "Class Width": 6.5,

}
print(df2)

extended_midpoints = [bins[0] - 3.5] + midpoints + [bins[-1] + 3.5]
extended_frequencies = [0] + frequencies + [0]

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].bar(labels, frequencies, width=0.5, color='steelblue', edgecolor='black')
axes[0].set_title('Histogram: Grams per Serving')
axes[0].set_xlabel('Class Interval')
axes[0].set_ylabel('Frequency')
axes[0].grid(axis='y')

axes[1].plot(extended_midpoints, extended_frequencies, marker='o', linestyle='-', color='navy')
axes[1].set_title('Frequency Polygon')
axes[1].set_xlabel('Midpoint')
axes[1].set_ylabel('Frequency')
axes[1].grid()

x = np.array(midpoints)
y = np.array(frequencies)
smooth_x = np.linspace(x.min(), x.max(), 500)
spline = make_interp_spline(x, y, k=2)
smooth_y = spline(smooth_x)

axes[2].plot(smooth_x, smooth_y, color='green')
axes[2].set_title('Frequency Curve')
axes[2].set_xlabel('Midpoint')
axes[2].set_ylabel('Frequency')
axes[2].grid()

plt.tight_layout()
plt.show()
