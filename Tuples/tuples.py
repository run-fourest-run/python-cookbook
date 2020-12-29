from geopy.geocoders import Nominatim
# Tuples

# Tuples can be used as either immutable lists or as records with no headers.
# If you think of a tuple simply as an immutable list then the quandity and order of the items may or may not be important
# But when tuple is used as a collection of fields, the number of items is often fixed and their order is always vital
# Therefore sorting a tuple destroys it's meaning -> Because the meaning of each data item/member is positional


homes = ['67 Bonnet Point Road', '3060 West Desert Crest Pl','500 W 1st St, Tempe AZ','286 2nd St New York']

geolocation = Nominatim(user_agent='test')



# if we sort the tuple at all we destroy the tuple
def get_coordinates(home):
    location = geolocation.geocode('{}'.format(home))
    latitude = location.latitude
    longitude = location.longitude
    coordinates = (latitude, longitude)
    return coordinates

coordinates = [get_coordinates(x) for x in homes]


for coordinate in sorted(coordinates):
    print('%s,%s' % coordinate)




## example 2

lax_coordinates = get_coordinates('Los Angeles International Airport')

#you can assign multiple variables to a tuple
city,year,pop,chg,area =('Tokyo',2003,2323242,0.55,8014)

# % String Formatting Operator knows tuple and treats each item at at's own field.
travelers_id = [('USA','2343225'),('BRA','3435326u7')]
for passport in sorted(travelers_id):
    print('%s/%s'% passport)



## Example 3 - Tuple Unpacking
original_home = homes[0]
test_coordinates = get_coordinates(original_home)
latitude,longitude = test_coordinates
print(latitude)
print(longitude)



## Example 4 - Tuple unpacking - Prefixing a Star to functions

test_ints = (1,2,3)

def test_function(x,y,z):
    val = x + y - z
    return val

test = test_function(*test_ints)
print(test)


alex_attributes = ('Alexander','USA','white','Male')
name,country,race,gender = alex_attributes

def test_function2(*alex_attributes):
    return "{},{},{},{}".format(name,country,race,gender)

print(test_function2(alex_attributes))

