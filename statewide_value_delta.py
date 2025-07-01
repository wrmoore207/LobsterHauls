# Year over year change in poundage
import pandas as pd 
import matplotlib.pyplot as plt 

def run_statewide_value_delta():
    # Get the data
    df = pd.read_csv('Data\preprocessed_data.csv')
    df = df.drop(columns=['Unnamed: 0'])

    # Separate statewide totals and county-level data
    statewide = df[df['COUNTY'] == 'Total'].copy()
    statewide = statewide.drop(columns=['FIPS'])

    # county_level = df[df['COUNTY'] != 'Total'].copy()

    # Rename columns for clarity
    statewide = statewide.rename(columns={'VALUE': 'total_value'})
    # county_level = county_level.rename(columns={'POUNDS': 'pounds', 'VALUE': 'value'})

    # Ensure YEAR is treated as a numeric column
    statewide['YEAR'] = pd.to_numeric(statewide['YEAR'])
    # county_level['YEAR'] = pd.to_numeric(county_level['YEAR'])

    # Statewide YoY Percent Change
    statewide['value_yoy'] = statewide['total_value'].pct_change() * 100

    # County-Level YoY Percent Change
    # county_level['pounds_yoy'] = county_level.groupby('COUNTY')['pounds'].pct_change() * 100
    # county_level['value_yoy'] = county_level.groupby('COUNTY')['value'].pct_change() * 100

    # Statewide Year-Over-Year Line Plot
    plt.figure(figsize=(10, 6))
    plt.plot(statewide['YEAR'], statewide['value_yoy'], label='Value YoY (%)', marker='o')
    plt.title('Statewide Year-Over-Year Change in Lobster Fishery Value')
    plt.xlabel('Year')
    plt.ylabel('Percent Change (%)')
    plt.legend()
    plt.grid()
    plt.savefig("Figs/StatewideRevenueDelta.svg")
    plt.show()


