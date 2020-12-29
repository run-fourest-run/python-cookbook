import math


class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __iter__(self):
        return (i for i in (self.x,self.y))

    def __format__(self, format_spec=''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self),self.angle())
            outer_format = '<{}, {}>'
        else:
            coords = self
            outer_format = '({},{})'
        components = (format(c,format_spec) for c in coords)
        return outer_format.format(*components)

    def __abs__(self):
        return math.hypot(self.x,self.y)

    def angle(self):
        return math.atan2(self.y,self.x)



v1 = Vector2D(1,2)
print(format(v1,'p'))