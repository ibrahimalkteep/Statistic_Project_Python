import pandas as pd
from scipy.stats import gmean, hmean
import numpy as np
import matplotlib.pyplot as plt

data = [469, 160, 125, 155, 475, 850, 100, 120, 100, 842, 765, 900, 145, 678, 122, 760]

s = pd.Series(data)

sample_size = s.count()
mean = s.mean()
median = s.median()
mode = s.mode().tolist()
minimum = s.min()
maximum = s.max()
range_val = maximum - minimum
first_quartile = s.quantile(0.25)
second_quartile = s.quantile(0.50) 
third_quartile = s.quantile(0.75)
iqr = third_quartile - first_quartile
variance = s.var()
std_dev = s.std()

geometric_mean = gmean(s)
harmonic_mean = hmean(s)

cv_percent = (std_dev / mean) * 100 if mean != 0 else 0


stats_dict = {
    "Sample size (n)": sample_size,
    "Mean": mean,
    "Median": median,
    "Mode": mode,
    "Geometric Mean": geometric_mean,
    "Harmonic Mean": harmonic_mean,
    "Minimum": minimum,
    "Maximum": maximum,
    "Range": range_val,
    "First Quartile": first_quartile,
    "Second Quartile": second_quartile,
    "Third Quartile": third_quartile,
    "Inter-Quartile Range": iqr,
    "Variance": variance,
    "Standard Deviation": std_dev,
    "CV %": cv_percent
}

df = pd.DataFrame(list(stats_dict.items()), columns=["Statistic", "Value"])

for stat, value in stats_dict.items():
    if isinstance(value, list):
        print(f"{stat}: {', '.join(map(str, value))}")
    else:
        print(f"{stat}: {value:.2f}" if isinstance(value, (float, np.float64)) else f"{stat}: {value}")

fig, axs = plt.subplots(1, 1, figsize=(4.5, 4.5))
fig.suptitle('Descriptive Statistics Table', fontsize=16)

table_text = df.to_string(index=False)
axs.axis('off')
axs.text(0.5, 0.95, table_text, fontfamily='monospace', fontsize=10, verticalalignment='top', horizontalalignment='center')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()