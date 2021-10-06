import pandas as panda
from geopy.geocoders import Nominatim
import numpy as np

df = panda.read_json("files\meteoritedata.json")

panda.set_option('display.max_columns', None)
panda.set_option('display.max_rows', None)
panda.set_option('display.width', None)

df = panda.concat([df.drop(['geolocation'], axis=1), df['geolocation'].apply(panda.Series)], axis=1)
df.drop(columns=['type', 0, ':@computed_region_cbhk_fwbd',  ':@computed_region_nnqa_25f4'], inplace=True)

geolocator = Nominatim(user_agent="script")

def getCountry(coords):
    if np.isnan(coords).any():
        return "NaN"
    elif type(coords) == list and len(coords) == 2: 
        lat, long = coords[1], coords[0]
        if np.isnan(lat) or np.isnan(long) or lat < -90 or lat > 90 or long < -180 or long > 180:
            return("NaN")
        else:
            location = geolocator.reverse((lat, long), timeout=None)
            if location is None:
                return("NaN")
            else: 
                country = location.address.split(', ')[-1]
                return country


def getCountry2(lat, long):
    if np.isnan(lat) or np.isnan(long) or lat < -90 or lat > 90 or long < -180 or long > 180:
        return 'NaN'
    elif (type(lat) == float and lat != None) and (type(long) == float and long != None):
        location = geolocator.reverse((lat, long), timeout=None)
        if location is None:
            return("NaN")
        else: 
            country = location.address.split(', ')[-1]
            return country

       
df['locations'] = df['coordinates'].apply(lambda x: getCountry(x))
df['locations2'] = df.apply(lambda x: getCountry2(x['reclat'], x['reclong']), axis=1)
print(df['locations'].equals(df['locations2']))
print(df)

small = list(range(0,2000))
medium = list(range(2001, 10000))
large = list(range(10001, df.mass.max().astype(int)))

smallAsteroids = df[df.mass.isin(small)]
mediumAsteroids = df[df.mass.isin(medium)]
largeAsteroids = df[df.mass.isin(large)]

smallAsteroids.to_csv('files\smallAsteroids.csv')
mediumAsteroids.to_csv('files\mediumAsteroids.csv')
largeAsteroids.to_csv('files\largeAsteroids.csv')