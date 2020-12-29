import copy


class Bus:
    def __init__(self,passengers = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self,passenger):
        self.passengers.append(passenger)

    def drop(self,passanger):
        self.passengers.remove(passanger)



'''You don't want parameters to be mutable types'''
class HauntedBus:
    def __init__(self,passengers=[]):
        self.passengers = passengers

    def pick(self,passenger):
        self.passengers.append(passenger)

    def drop(self,passenger):
        self.passengers.remove(passenger)

'''
first thing we are going to demonstrate is deep and shallow copies of arbitrary objects

'''


class Squad:
    def __init__(self,mates):
        if mates is None:
            self.mates = []
        else:
            self.mates = list(mates)

    def __iter__(self):
        return (x for x in (self.mates))

    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r})'


warzone_squad = Squad(['alexander','spencer','Jared'])
print(warzone_squad)
warzone_squad_copy = copy.copy(warzone_squad)