import pandas as pd
import numpy as np
import gmaps
import gmaps.datasets
import dataset as dataset
import gmaps_apikey as gak # API key for Google Maps
import math
import pdb
# Load the datasets
crime_data = dataset.get_dataset()
crime_data.head()

Latitude = crime_data['Latitude']
Longitude = crime_data['Longitude']

# Q: What is the longitude of ney york city?
# A: -74.0059413 to -73.910408
Lon = np.arange(-74.0059413, -73.910408, 0.021) # 0.021 is the step size

# Q: What is the latitude of ney york city?
# A: 40.5774 to 40.917577
Lat = np.arange(40.5774, 40.917577, 0.021) # 0.021 is the step size

Crime_counts = np.zeros((1000,1000)) # 1000x1000 matrix

gmaps.configure(api_key = gak.getApiKey())

heatmap_data = {'Latitude':  Latitude, 'Longitude': Longitude}
# make heatmap data a one-dimensional array
np.concatenate(list(heatmap_data.values()))
df = pd.DataFrame(data=heatmap_data)
locations = df[['Latitude', 'Longitude']]
weights = df['Latitude']
fig = gmaps.figure()
cleaned_locs = []
cleaned_weights = []
ghts = []
for i in range(len(locations)):
    if type(locations['Latitude'][i]) != str and not math.isnan(locations['Latitude'][i]) and not math.isnan(locations['Latitude'][i]):
        if type(locations['Longitude'][i]) != str and not math.isnan(locations['Longitude'][i]) and not math.isnan(locations['Longitude'][i]):
            cleaned_locs.append((locations['Latitude'][i], locations['Longitude'][i]))
        
for i in weights:
    if not math.isnan(i):
        cleaned_weights.append(i)
        
heatmap_layer = gmaps.heatmap_layer(cleaned_locs, weights=cleaned_weights)
fig.add_layer(heatmap_layer)
pdb.set_trace() # Display the heatmap
