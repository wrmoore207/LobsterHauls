'''
Open the file .txt file, preprocess and save it as a .csv
intended to be run once prior to running visualizations
Access the .csv file itself rather than re-run preprocessing every time or keep all viz in one long file. 
'''

import pandas as pd

def run_preprocessing():

    # Load the data
    file_path = "Data/countyLobsters.txt"

    data = pd.read_csv(file_path, delim_whitespace=True)

    print(data.shape)
    '''
    Preprocessing and Filtering
    '''
    # Convert the 'POUNDS' column to integers
    data['POUNDS'] = data['POUNDS'].str.replace(',', '').astype(int)

    # Remove the dollar signs and commas, then convert to integers
    data['VALUE'] = data['VALUE'].str.replace(r'[\$,]', '', regex=True).astype(int)

    # List of counties to drop
    counties_to_drop = ['NOT-SPECIFIED', 'KNOX/WALDO', 'UNKNOWN']

    # Filter the data to exclude the specified counties
    filtered_data = data[~data['COUNTY'].isin(counties_to_drop)]

    # Update the COUNTY column to have title case
    filtered_data['COUNTY'] = filtered_data['COUNTY'].str.title()

    county_to_fips = {
        "Androscoggin": "001",
        "Aroostook": "003",
        "Cumberland": "005",
        "Franklin": "007",
        "Hancock": "009",
        "Kennebec": "011",
        "Knox": "013",
        "Lincoln": "015",
        "Oxford": "017",
        "Penobscot": "019",
        "Piscataquis": "021",
        "Sagadahoc": "023",
        "Somerset": "025",
        "Waldo": "027",
        "Washington": "029",
        "York": "031"
    }

    filtered_data['FIPS'] = filtered_data['COUNTY'].map(county_to_fips)

    # Save the data as a .csv for consistency
    filtered_data.to_csv('Data/preprocessed_data.csv', index=True)
