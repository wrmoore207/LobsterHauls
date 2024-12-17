import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv('Data\preprocessed_data.csv')

# Filter out "Total" for this plot
counties = df[df['COUNTY'] != 'Total']

plt.figure(figsize=(12, 8))
for county in counties['COUNTY'].unique():
    county_data = counties[counties['COUNTY'] == county]
    plt.plot(
        county_data['YEAR'], 
        county_data['POUNDS'] / 1e6,  # Scale pounds to millions
        marker='o', 
        label=county
    )

# Add labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Pounds (in Millions)')
plt.title('Lobster Pounds by County Over the Years')
plt.legend(title='County', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.tight_layout()
plt.savefig("Figs/PoundsByCounty.svg")
plt.show()