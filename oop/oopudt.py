from array import array
from math import hypot

class Vector:

    typecode = 'd'
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x,self.y))


    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode,self)))

    def __abs__(self):
        return hypot(self.x,self.y)

    def __add__(self, other):
        x = self.x + other
        y = self.y + other
        return Vector(x,y)

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __repr__(self):
        class_name = type(self).__name__
        return '{}{!r},{!r})'.format(class_name, *self)


class Vector3d:
    def __init__(self,x,y,z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __iter__(self):
        return (i for i in (self.x,self.y,self.z))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r}.{!r})'.format(class_name,*self)



class Node:
    def __init__(self,node_id,parent_id,resource,layer):
        self.node_id = node_id
        self.parent_id = parent_id
        self.resource = resource
        self.layer = layer

    def __iter__(self):
        return (i for i in (self.node_id,self.parent_id,self.resource,self.layer))

    def __repr__(self):
        return ''









'''
v1 = Vector(3,4)
v2 = Vector(4,5)
v3 = Vector3d(1,3,4)
v4 = Vector3d(1,4,5)
v5 = Vector3d(1,4,5)

point_x,point_y = v1
print(point_x,point_y)
point_x,point_y = v2
print(point_x,point_y)
point_x,point_y,point_z = v3
print(point_x,point_y,point_z)
point_x,point_y,point_z = v4
print(point_x,point_y,point_z)


print(v4.__repr__())

'''