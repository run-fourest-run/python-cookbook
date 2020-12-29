from collections import namedtuple
from geopy.geocoders import Nominatim
import os

geolocation = Nominatim(user_agent='test')
homes = ['67 Bonnet Point Road', '3060 West Desert Crest Pl', '500 W 1st St, Tempe AZ', '286 2nd St New York']
narragansett_population = ('Narragansett', 50000)
tucson_population = ('Tucson', 350000)
tempe_population = ('Tempe', 500000)
newyork_population = ('New York', 7500000)
populations = []
populations.append(narragansett_population)
populations.append(tucson_population)
populations.append(tempe_population)
populations.append(newyork_population)


# if we sort the tuple at all we destroy the tuple
def get_coordinates(home):
    location = geolocation.geocode('{}'.format(home))
    latitude = location.latitude
    longitude = location.longitude
    coordinates = (latitude, longitude)
    return coordinates


coordinates = [get_coordinates(x) for x in homes]
print(coordinates)


def get_coordinates_and_population(coordinates, populations):
    new_list_of_populations_coordinates = []
    for coordinate in coordinates:
        for coordinate in coordinates:
             coordinates_populations_tuple = populations + (coordinate,)
             new_list_of_populations_coordinates.append(coordinates_populations_tuple)
    return new_list_of_populations_coordinates

x = get_coordinates_and_population(coordinates,populations)
for val in x:
    print(x)



