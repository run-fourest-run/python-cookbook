import datetime
import random

'''
An object is hashable if it implements both the __hash__ & the __eq__ method. The Object must create
one immutable integer to be compared equal to other instances.

'''



import math

class Vector2d:

    typecode = 'd'
    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.x,self.y))

    @property
    def x(self,x):
        return self.__x

    @property
    def y(self,y):
        return self.__y

    def __format__(self, format_spec):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self),self.angle())
            outer_format = '<{},{}>'
        else:
            coords = self
            outer_format = '({},{})'
        components = (format(c,format_spec) for c in coords)
        return outer_format.format(*components)

    def __abs__(self):
        return math.hypot(self.x,self.y)

    def angle(self):
        return math.atan2(self.y,self.x)



v1 = Vector2d(1,2)
'''


class ImmutablePerson:
    def __init__(self,firstname,birthday):
        self.__firstname = firstname
        self.__birthday = birthday

    @property
    def firstname(self):
        return self.__firstname
    @property
    def birthday(self):
        return self.__birthday

    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r},{!r})'.format(classname,self.__firstname,self.__birthday)


class MutablePerson:
    def __init__(self,firstname,lastname,birthday):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday


    def __iter__(self):
        return (i for i in (self.firstname,self.lastname,self.birthday))

    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r},{!r},{!r})'.format(classname,self.firstname,self.lastname)

'''









class MutablePersonPerson:
    def __init__(self,firstname,lastname,birthday):
        self.firstname = firstname
        self.lastname = lastname
        self.birthday= birthday

    def __iter__(self):
        return (i for i in (self.firstname,self.lastname,self.birthday))


    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r},{!r},{!r})'.format(classname)


#pass in a list instead of the individual things
class ImmutablePerson:
    def __init__(self, firstname,lastname,birthday,birthmonth,birthyear):
        self.firstname = firstname
        self.lastname = lastname
        self.__birthday = birthday
        self.__birthmonth = birthmonth
        self.__birthyear = birthyear

    def __iter__(self):
        return (i for i in (self.firstname,self.lastname,self.birthday,self.birthmonth,self.birthyear))


    @property
    def birthday(self):
        return self.__birthday

    @property
    def birthmonth(self):
        return self.__birthmonth

    @property
    def birthyear(self):
        return self.__birthyear


    def __repr__(self):
        classname = type(self).__name__
        return "{}({!r},{!r},{!r})".format(classname,self.firstname,self.lastname,self.birthday)









