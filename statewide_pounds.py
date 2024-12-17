import matplotlib.pyplot as plt
import pandas as pd 

# Load the data
df = pd.read_csv('Data/preprocessed_data.csv')

# Filter to only include the "Total" county
total_data = df[df['COUNTY'] == 'Total']

# Plot data for the "Total" county
plt.figure(figsize=(12, 8))
plt.plot(
    total_data['YEAR'], 
    total_data['POUNDS'] / 1e6,  # Scale pounds to millions
    marker='o', 
    label='Total'
)

# Add labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Pounds (in Millions)')
plt.title('Lobster Pounds - Total Over the Years')
plt.legend(title='County')
plt.grid()
plt.tight_layout()

# Save and display the plot
plt.savefig("Figs/TotalPoundsByYear.svg")
plt.show()