'''
Testing class attributes - I want to see if I can return a class attribute easily or how that really works from a reference perspective
'''



class Sensor:
    static = 'test'

    def __init__(self):
        pass


    def _print_class_attribute(self):
        return self.static



test_class_attribute = Sensor()
print(type(test_class_attribute))

print(test_class_attribute._print_class_attribute())


