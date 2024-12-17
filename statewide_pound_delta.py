'''
Year over year change in poundage
Calculated by determining the increase or decrease from the year before
ie: if 100 lobsters were caught it 1999 and 120 were caught in 2000, that's a 20% increase

Initial analysis will be done on Totals first for POC, then individual counties plotted individually

'''

import pandas as pd 
import matplotlib.pyplot as plt 

# Get the data
df = pd.read_csv('Data\preprocessed_data.csv')
df = df.drop(columns=['Unnamed: 0'])

# Separate statewide totals and county-level data
statewide = df[df['COUNTY'] == 'Total'].copy()
statewide = statewide.drop(columns=['FIPS'])

# county_level = df[df['COUNTY'] != 'Total'].copy()

# Rename columns for clarity
statewide = statewide.rename(columns={'POUNDS': 'total_pounds', 'VALUE': 'total_value'})
# county_level = county_level.rename(columns={'POUNDS': 'pounds', 'VALUE': 'value'})

# Ensure YEAR is treated as a numeric column
statewide['YEAR'] = pd.to_numeric(statewide['YEAR'])
# county_level['YEAR'] = pd.to_numeric(county_level['YEAR'])

# Statewide YoY Percent Change
statewide['pounds_yoy'] = statewide['total_pounds'].pct_change() * 100

# County-Level YoY Percent Change
# county_level['pounds_yoy'] = county_level.groupby('COUNTY')['pounds'].pct_change() * 100
# county_level['value_yoy'] = county_level.groupby('COUNTY')['value'].pct_change() * 100

# Statewide Year-Over-Year Line Plot
plt.figure(figsize=(10, 6))
plt.plot(statewide['YEAR'], statewide['pounds_yoy'], label='Pounds YoY (%)', marker='o')
plt.title('Statewide Year-Over-Year Change in Total Lobster Haul by Weight')
plt.xlabel('Year')
plt.ylabel('Percent Change (%)')
plt.legend()
plt.grid()
plt.savefig("Figs/StatewidePoundDelta.svg")
plt.show()
