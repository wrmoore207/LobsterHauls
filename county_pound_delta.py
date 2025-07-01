import pandas as pd 
import matplotlib.pyplot as plt 
def run_county_pound_delta():
    # Get the data
    df = pd.read_csv('Data\preprocessed_data.csv')
    df = df.drop(columns=['Unnamed: 0'])

    # Separate statewide totals and county-level data
    county_level = df[df['COUNTY'] != 'Total'].copy()

    # Rename columns for clarity
    county_level = county_level.rename(columns={'POUNDS': 'pounds', 'VALUE': 'value'})

    # Ensure YEAR is treated as a numeric column
    county_level['YEAR'] = pd.to_numeric(county_level['YEAR'])

    # County-Level YoY Percent Change
    county_level['pounds_yoy'] = county_level.groupby('COUNTY')['pounds'].pct_change() * 100
    # county_level['value_yoy'] = county_level.groupby('COUNTY')['value'].pct_change() * 100

    # Small Multiples for County-Level Pounds YoY
    # Define unique counties and grid layout
    unique_counties = county_level['COUNTY'].unique()
    num_cols = 4
    num_rows = -(-len(unique_counties) // num_cols)  # Calculate rows needed, rounding up

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 3 * num_rows), sharey=False)
    axes = axes.flatten()  # Flatten axes to loop through them easily

    # Loop through each county and create a subplot
    for i, county in enumerate(unique_counties):
        county_data = county_level[county_level['COUNTY'] == county]
        axes[i].plot(county_data['YEAR'], county_data['pounds_yoy'], marker='o', linestyle='-')
        axes[i].set_title(county)
        axes[i].set_xlabel('Year')
        axes[i].set_ylabel('Pounds YoY (%)')
        axes[i].grid()

    plt.tight_layout()
    plt.savefig("Figs/CountyPoundDelta.svg")
    plt.show()
