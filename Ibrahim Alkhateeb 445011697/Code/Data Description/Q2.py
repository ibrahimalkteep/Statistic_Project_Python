import pandas as pd
import matplotlib.pyplot as plt

grades_data = { 
    'Grade': ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A'],
    'Number of Students': [8, 10, 15, 40, 25, 10, 7, 5]
}

df = pd.DataFrame(grades_data)

df['Relative Frequency'] = df['Number of Students'] / df['Number of Students'].sum()
df['Relative Frequency (%)'] = df['Relative Frequency'] * 100

print(df)

fig, axes = plt.subplots(2, 2, figsize=(12, 6))


axes[0,0].bar(df['Grade'], df['Number of Students'], color='skyblue')
axes[0,0].set_title('Bar Chart: Grades')
axes[0,0].set_xlabel('Grade')
axes[0,0].set_ylabel('Number of Students')
axes[0,0].grid(axis='y')


for i, v in enumerate(df['Number of Students']):
    axes[0,0].text(i, v, str(v), ha='center', va='bottom')


axes[0,1].pie(df['Number of Students'], labels=df['Grade'], autopct='%1.1f%%', startangle=90)
axes[0,1].set_title('Pie Chart: Grades')
axes[0,1].axis('equal')

table_text = df.to_string(index=False)
axes[1,0].axis('off')
axes[1,0].text(0.5, 0.95, table_text, fontfamily='monospace', fontsize=10, verticalalignment='top', horizontalalignment='center')

axes[1, 1].axis('off')

plt.tight_layout()
plt.show()
