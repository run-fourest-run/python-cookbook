class HauntedBus:
    def __init__(self,passengers = []):
        self.passengers = passengers

    def pick(self,name):
        return self.passengers.append(name)


    def drop(self,name):
        return self.passengers.remove(name)

class GreatBus:
    def __init__(self,passengers = []):
        if self.passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pickup(self,passenger):
        return self.passengers.append(passenger)

    def dropoff(self,passenger):
        return self.passengers.remove(passenger)

class Concert:
    def __init__(self,acts):
        if self.acts is None:
            self.acts = []
        else:
            self.acts = list(acts)

    def add_act(self,act):
        return self.acts.append(act)

    def remove_act(self,act):
        return self.acts.remove(act)



'''
Haunted Bus illustrates how if you pass a mutable parameter there will be problems in situations where you
instantiate the object with no arguements. In that case any subsequent objects will share the same attributes


'''

hauntedbus = HauntedBus(passengers=['john','alice','cory'])
hauntedbus_2 = HauntedBus()
hauntedbus_2.pick('james')
print("this is the haunted bus passengers %s" % (hauntedbus.passengers))
print("This is the copy haunted bus passengers %s" %(hauntedbus_2.passengers))
hauntedbus_3 = HauntedBus()
hauntedbus_3.pick('alan')
print("This is the copy haunted bus passengers %s" %(hauntedbus_2.passengers))
print("This is the copy copy haunted bus passengers %s" %(hauntedbus_3.passengers))


