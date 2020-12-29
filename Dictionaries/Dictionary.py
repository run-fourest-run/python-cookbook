'''
* Dictionaries are widely used in python. Probably the most widely used datastructure.
* Hash tables are the engines behind Pythons high-performance dicts.


'''


'''
What is hashable?

An object is Hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method ) and can be compared to other
objects (it needs an __eq__() method) Hashable objects which compare equal must have the same hash value

'''



tt = (1,10,(5,20))
# print(hash(tt))

tt_new = (1,10,(5,20))
# print(hash(tt_new))
# print(hash(tt) == hash(tt_new))




'''
different ways to build a dict

'''

a = dict(one=1 , two=2, three= 3)
b = {'one': 1, 'two':2,'three':3}
c = dict(zip(['one','two','three'],[1,2,3]))
d = dict([('two',2),('one',1),('three',3)])
e = dict({'one':1, 'two':2, 'three':3})


'''
Dict Comprehension
'''

DIAL_CODES = [
(86, 'China'),
(91, 'India'),
(1, 'United States'),
(62, 'Indonesia'),
(55, 'Brazil'),
(92, 'Pakistan'),
(880, 'Bangladesh'),
(234, 'Nigeria'),
(7, 'Russia'),
(81, 'Japan')]




dict_comp = {country: code for code, country in DIAL_CODES}

new_dict_comp = {code: country.upper() for code,country in DIAL_CODES if code > 40 and code < 100}

# How to iterate through a dictionary. You need to apply the .items() method to the end of the iterable -> It's not immediately clear why.\

# Naked iteration will return the keys
'''
for key in dict_comp:
    print(key)
'''
# You need .items if you want to get the value from the dictionary.
'''
for key,value in dict_comp.items():
    print(value)
'''


for key,value in new_dict_comp.items():
    print(key,value)

