'''
Class Method:
define a method that operates on the class and not the instance itself.
classmethod decorator changes the way the method is called, so it recives the class itself as it's first arguement.
It's most common use is for alternative constructors.

ex: .fromBytes


Static Method decorator:
defines a method that changes a method so that it recieves no special first arguement. In essense it's a plain function that happens to live in
a class body. instead of being defined at the module level

'''


class Demo:

    @staticmethod
    def statmeth(*args):
        return args

    @classmethod
    def klassmeth(*args):
        return args


d1 = Demo()

print(d1.statmeth('test'))
print(d1.klassmeth('test'))