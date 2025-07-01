import pandas as pd 
import matplotlib.pyplot as plt 

def run_state_per_pound():
    # Get the data
    df = pd.read_csv('Data\preprocessed_data.csv')

    # Extract Statewide data using 'Total' rows
    state_level = df[df['COUNTY'] == 'Total'].copy()

    # Calculate price per pound
    state_level['price_per_pound'] = state_level['VALUE'] / state_level['POUNDS']

    # Statewide Price Per Pound Over Time
    plt.figure(figsize=(10, 6))
    plt.plot(state_level['YEAR'], state_level['price_per_pound'], marker='o', linestyle='-', label='Price Per Pound')
    plt.title('Statewide Price Per Pound Over Time')
    plt.xlabel('Year')
    plt.ylabel('Price Per Pound (USD)')
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig("Figs/StatePricePerPound.svg")
    plt.show()