import time
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent = 'exercisesGEOPY')

def get_data(x):
  index, row = x 
  time.sleep( 1 ) #this is to not overload the API and get kicked-out
    
  #Call API
  response = geolocator.reverse(row['query'])
  address = response.raw['address']
    
  #Get the responses, if it comes back empty it will return NA
  place_id = response.raw['place_id'] if 'place_id' in response.raw else 'NA' 
  osm_type = response.raw['osm_type'] if 'osm_type' in response.raw else 'NA' 
  country = response.raw['address']['country'] if 'country' in address else 'NA' 
  country_code = response.raw['address']['country_code'] if 'country_code' in address else 'NA' 
    
  #And return as an output from the function
  return place_id, osm_type, country, country_code 