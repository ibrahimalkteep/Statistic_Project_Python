import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

first_midterm = np.array([12, 18, 20, 22, 21, 17, 19, 10])
final_midterm = np.array([61, 67, 68, 78, 70, 85, 79, 65])

correlation = np.corrcoef(final_midterm, first_midterm)[0, 1]

slope, intercept, r_value, p_value, std_err = linregress(final_midterm, first_midterm)

X_value = 24
y_pred = intercept + slope * X_value

results_text = (
    f"{'Description':<40} {'Value'}\n"
    f"{'-'*60}\n"
    f"{'Correlation Coefficient':<40} {correlation:.8f}\n"
    f"{'Slope (b)':<40} {slope:.8f}\n"
    f"{'Intercept (a)':<40} {intercept:.8f}\n"
    f"{'Linear Regression':<40} y = {intercept:.8f} + {slope:.8f}*X\n"
    f"{f'X = {X_value}':<40} y = {y_pred:.8f}"
)

fig, axs = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})

axs[0].plot(range(1, len(first_midterm) + 1), first_midterm, marker='o', label='First Midterm')
axs[0].plot(range(1, len(final_midterm) + 1), final_midterm, marker='o', label='Final Midterm')

axs[0].set_title("Scatter Plot")
axs[0].set_xlabel("Student Index")
axs[0].set_ylabel("Scores")
axs[0].legend()
axs[0].grid(True)

axs[1].axis("off")
axs[1].text(0, 1, results_text, fontsize=11, fontfamily='monospace', va='top')

plt.tight_layout()
plt.show()
