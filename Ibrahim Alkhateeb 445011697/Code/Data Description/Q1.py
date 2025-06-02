import pandas as pd
import matplotlib.pyplot as plt

trust_data = ['A'] * 4 + ['M'] * 28 + ['H'] * 6 + ['S'] * 2 

trust_series = pd.Series(trust_data) 
freq = trust_series.value_counts()
rel_freq = freq / len(trust_series)
rel_freq_percent = rel_freq * 100
names  = ['M', 'H', 'A', 'S']
table = pd.DataFrame({
    '' : names,
    'Frequency': freq,
    'Relative Frequency': rel_freq,
    'Relative Frequency (%)': rel_freq_percent
})

print(table)

fig, axes = plt.subplots(2, 2, figsize=(12, 5))

table_text = table.to_string(index=False)
axes[1,0].axis('off')
axes[1,0].text(0.5, 0.95, table_text, fontfamily='monospace', fontsize=10, verticalalignment='top', horizontalalignment='center')

bars = freq.plot(kind='bar', ax=axes[0,0], color='skyblue') 
axes[0,0].set_title('Bar Chart: Trust in Internet') 
axes[0,0].set_xlabel('Category')
axes[0,0].set_ylabel('Frequency')
axes[0,0].grid(axis='y') 

for i, v in enumerate(freq):
    axes[0,0].text(i, v, str(v), ha='center', va='bottom')


freq.plot(kind='pie', ax=axes[0,1], autopct='%1.1f%%', title='Pie Chart: Trust in Internet')
axes[0,1].set_ylabel('')  

axes[1, 1].axis('off')

plt.tight_layout()
plt.show()
