import pandas as panda
from geopy.geocoders import Nominatim
import numpy as np
import pandas_schema as ps

df = panda.read_json("files\meteoritedata.json")

panda.set_option('display.max_columns', None)
panda.set_option('display.max_rows', None)
panda.set_option('display.width', None)

df = panda.concat([df.drop(['geolocation'], axis=1), df['geolocation'].apply(panda.Series)], axis=1)
df.drop(columns=['type', 0, ':@computed_region_cbhk_fwbd',  ':@computed_region_nnqa_25f4'], inplace=True)

geolocator = Nominatim(user_agent="script")

def getCountry(coords):
    if type(coords) == list and len(coords) == 2: 
        lat, long = coords[1], coords[0]
        if checkLat(lat) == False or checkLong(long) == False:
            return None
        else:
            location = geolocator.reverse((lat, long), timeout=None, language='en')
            if location is None:
                return None
            else: 
                country = location.address.split(', ')[-1]
                return str(country).strip()
    else:
        return None


def getCountry2(lat, long):
    if checkLat(lat) == False or checkLong(long) == False:
        return None
    else:
        location = geolocator.reverse((lat, long), timeout=None, language='en')
        if location is None:
            return None
        else: 
            country = location.address.split(', ')[-1]
            return str(country)
     

def checkLat(latitude):
    if latitude == None:
        return False
    try:
        latitude = float(latitude)
        if type(latitude) != float or np.isnan(latitude) == True or latitude == None or latitude < -90 or latitude > 90:
            return False
        else:
            return True
    except ValueError:
        return False
    

def checkLong(longitude):
    if longitude == None: 
        return False
    try:
        longitude = float(longitude)
        if type(longitude) != float or np.isnan(longitude) == True or longitude == None or longitude < -180 or longitude > 180:
            return False
        else:
            return True
    except ValueError:
        return False

#df['locations'] = df['coordinates'].apply(lambda x: getCountry(x))
#df['locations2'] = df.apply(lambda x: getCountry2(x['reclat'], x['reclong']), axis=1)


#df['difference'] = np.where((df['locations'] == df['locations2']), "DIFFERENCE", None)
#print(df[['locations', 'locations2','difference']])

#sample = df[['locations', 'locations2', 'difference']].head(2) 
#sample['locationsLen'] = sample['locations'].str.len()
#sample['locations2Len'] = sample['locations2'].str.len()
#print(sample)

#small = list(range(0,2000))
#medium = list(range(2001, 10000))
#large = list(range(10001, df.mass.max().astype(int)))

#smallAsteroids = df[df.mass.isin(small)]
#ediumAsteroids = df[df.mass.isin(medium)]
#largeAsteroids = df[df.mass.isin(large)]

#smallAsteroids.to_csv('files\smallAsteroids.csv')
#mediumAsteroids.to_csv('files\mediumAsteroids.csv')
#largeAsteroids.to_csv('files\largeAsteroids.csv')