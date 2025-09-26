import pandas as pd

# Load the dataset with semicolon delimiter
df = pd.read_csv("istherecorrelation.csv", delimiter=';')

# Inspect the data
print(df.head())
print(df.info())

import matplotlib.pyplot as plt
import numpy as np

# Data Cleaning
# Clean the 'WO [x1000]' column: replace comma with period and convert to float
df['WO_x1000'] = df['WO [x1000]'].str.replace(',', '.').astype(float)
df.rename(columns={'NL Beer consumption [x1000 hectoliter]': 'NL_Beer_Consumption_x1000_hl'}, inplace=True)

# Calculate Pearson correlation coefficient
correlation = df['WO_x1000'].corr(df['NL_Beer_Consumption_x1000_hl'])

# Create the dual-axis plot
fig, ax1 = plt.subplots(figsize=(10, 6), dpi=300)

# Plot WO [x1000] on the primary axis (ax1)
color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('WO [x1000]', color=color)
ax1.plot(df['Year'], df['WO_x1000'], color=color, label='WO [x1000]', marker='o')
ax1.tick_params(axis='y', labelcolor=color)
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, linestyle='--', alpha=0.6)

# Create a secondary axis for NL Beer consumption (ax2)
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('NL Beer consumption [x1000 hl]', color=color)
ax2.plot(df['Year'], df['NL_Beer_Consumption_x1000_hl'], color=color, label='NL Beer consumption [x1000 hl]', marker='x')
ax2.tick_params(axis='y', labelcolor=color)

# Title and legend (combining legends from both axes)
fig.suptitle(f'Trends of WO and NL Beer Consumption (2006-2018)\nPearson Correlation: {correlation:.3f}', fontsize=16)

# Save the plot
plt.tight_layout()
plt.savefig('correlation_plot.png')

print(f"Pearson Correlation Coefficient: {correlation:.4f}")