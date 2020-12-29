from geopy.geocoders import Nominatim
import os



homes = ['67 Bonnet Point Road', '3060 West Desert Crest Pl','500 W 1st St, Tempe AZ','286 2nd St New York']
narragansett_population = ('Narragansett',1500000)
tucson_population = ('Tucson',2000000)
tempe_population = ('Tempe',1500000)
newyork_population = ('New York',25052)
populations = []
populations.append(narragansett_population)
populations.append(tucson_population)
populations.append(tempe_population)
populations.append(newyork_population)

geolocation = Nominatim(user_agent='test')



# if we sort the tuple at all we destroy the tuple
def get_coordinates(home):
    location = geolocation.geocode('{}'.format(home))
    latitude = location.latitude
    longitude = location.longitude
    coordinates = (latitude, longitude)
    return coordinates


coordinates = [get_coordinates(x) for x in homes]


def get_coordinates_and_population(coordinates,populations):
    new_list = []
    for population in populations:
        for coordinate in coordinates:
            coordinates_populations_tuple = population + (coordinate,)
            new_list.append(coordinates_populations_tuple)
    return new_list


list_of_tuples = get_coordinates_and_population(coordinates,populations)
print(list_of_tuples)
for town,population,coordinates in list_of_tuples:
    latitude,longitude = coordinates
    print('town={}, population={}, coordinates={}, latitude={}, longitude={}'.format(town,population,coordinates,latitude,longitude))



lax_coordinates = get_coordinates('Los Angeles International Airport')


# tuple unpacking using parrell assignment
# assigning items from an iterable to a tuple of variables


#example 1

latitude,longitude = lax_coordinates



# example 2

quotient,remainder = divmod(14,20)
#print(quotient)
#print(remainder)


# example 3
test_string = "this is a test string"


def tuple_string_splitter_unpacker(input_string):
    split_input_string = input_string.split()
    last_word = split_input_string[-1]
    tuple_string = tuple(split_input_string)
    return tuple_string,last_word

first_part, last_word  = tuple_string_splitter_unpacker(test_string)
# print(last_word)



## example 4

