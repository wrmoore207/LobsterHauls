'''
Data Sources:
https://www.fisheries.noaa.gov/foss/f?p=215:200:3318813416469:::CR,200::

https://www.maine.gov/dmr/science/weather-tides/boothbay-harbor-environmental-data

Library Docs:

Image Export
    https://plotly.com/python/static-image-export/
'''

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
pio.kaleido.scope.default_format = "svg"

# Load the data
file_path = "Data\countyLobsters.txt"
data = pd.read_csv(file_path, delim_whitespace=True)

'''
Preprocessing and Filtering
'''
# Convert the 'POUNDS' column to integers
data['POUNDS'] = data['POUNDS'].str.replace(',', '').astype(int)

# Remove the dollar signs and commas, then convert to integers
data['VALUE'] = data['VALUE'].str.replace('[\$,]', '', regex=True).astype(int)

# List of counties to drop
counties_to_drop = ['NOT-SPECIFIED', 'KNOX/WALDO', 'UNKNOWN', 'TOTAL']

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



'''
Visualizations
    [x] Annual Catch Over Time
    [x] Annual Catch by County Over Time
    [x] Value per Pound per county (Value/Pounds)
    [] Annual Value Over Time
    [] Choropleth of Value by County for most recent year
'''

# # [x] Annual Catch by County Over Time
# plt.figure(figsize=(12, 8))
# for county in filtered_data['COUNTY'].unique():
#     county_data = filtered_data[filtered_data['COUNTY'] == county]
#     plt.plot(
#         county_data['YEAR'], 
#         county_data['POUNDS'] / 1e6,  # Scale pounds to millions
#         marker='o', 
#         label=county
#     )

# # Add labels, title, and legend
# plt.xlabel('Year')
# plt.ylabel('Pounds (in Millions)')
# plt.title('Lobster Pounds by County Over the Years')
# plt.legend(title='County', bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.grid()
# plt.tight_layout()
# plt.show()

# # [x] Annual Catch Over Time
# total_data = data[data['COUNTY'] == 'TOTAL']

# plt.figure(figsize=(10, 6))
# plt.plot(
#     total_data['YEAR'], 
#     total_data['POUNDS'] / 1e6,
#     marker='o', 
#     color='red', 
#     label='Yearly Total'
# )

# plt.xlabel('Year')
# plt.ylabel('Total Pounds (in Millions)')
# plt.title('Total Lobster Pounds Over the Years')
# plt.legend()
# plt.grid()
# plt.tight_layout()
# plt.show()

# # [x] Value per Pound per county (Value/Pounds)
# plt.figure(figsize=(12, 8))
# for county in filtered_data['COUNTY'].unique():
#     county_data = filtered_data[filtered_data['COUNTY'] == county]
#     plt.plot(
#         county_data['YEAR'], 
#         county_data['VALUE']/1e6,
#         marker='o', 
#         label=county
#     )

# # Add labels, title, and legend
# plt.xlabel('Year')
# plt.ylabel('Value (in Millions)')
# plt.title('Lobster Value by County Over the Years')
# plt.legend(title='County', bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.grid()
# plt.tight_layout()
# plt.show()

# total_data = data[data['COUNTY'] == 'TOTAL']

# plt.figure(figsize=(10, 6))
# plt.plot(
#     total_data['YEAR'], 
#     total_data['VALUE'] / 1e6,
#     marker='o', 
#     color='red', 
#     label='Yearly Total'
# )

# plt.xlabel('Year')
# plt.ylabel('Total Dollar Value (in Millions)')
# plt.title('Total Lobster Value Over the Years')
# plt.legend()
# plt.grid()
# plt.tight_layout()
# plt.show()

import plotly.express as px

# Filter the data for the most recent year
latest_year = filtered_data['YEAR'].max()
latest_data = filtered_data[filtered_data['YEAR'] == latest_year]

import requests
import json

# Load the GeoJSON file
response = requests.get('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json')
geojson_data = response.json()

# Print the first few features to inspect their properties
print(json.dumps(geojson_data['features'][:5], indent=2))

# # Create the choropleth map
# fig = px.choropleth(
#     latest_data,
#     geojson='https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json',
#     locations='FIPS',  # Use the FIPS codes
#     featureidkey="properties.fips",  # Match GeoJSON's FIPS field
#     color='VALUE',
#     hover_name='COUNTY',
#     color_continuous_scale='Viridis',
#     title=f"Lobster Value by County for {latest_year}"
# )

# # Update the layout for better visualization
# fig.update_geos(
#     visible=False,
#     projection_type="albers usa"
# )
# fig.update_layout(
#     margin={"r":0,"t":0,"l":0,"b":0},
#     coloraxis_colorbar=dict(title="Value (in $)")
# )

# # Show the map
# fig.show()
