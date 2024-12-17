import pandas as pd 
import matplotlib.pyplot as plt 

# Get the data
df = pd.read_csv('Data\preprocessed_data.csv')

# County-Level price per pound (excluding 'Total')
county_level = df[df['COUNTY'] != 'Total'].copy()
county_level['price_per_pound'] = county_level['VALUE'] / county_level['POUNDS']

# Small Multiples for County-Level Price Per Pound
unique_counties = county_level['COUNTY'].unique()
num_cols = 4
num_rows = -(-len(unique_counties) // num_cols)  # Round up to calculate rows

fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 3 * num_rows), sharey=True)
axes = axes.flatten()

for i, county in enumerate(unique_counties):
    county_data = county_level[county_level['COUNTY'] == county]
    axes[i].plot(county_data['YEAR'], county_data['price_per_pound'], marker='o', linestyle='-')
    axes[i].set_title(county)
    axes[i].set_xlabel('Year')
    axes[i].set_ylabel('Price Per Pound (USD)')
    axes[i].grid()

plt.tight_layout()
plt.savefig("Figs/CountyPricePerPound.svg")

plt.show()
