

#Showing how an object is instantiated first before being assigned to a variable
class Person:
    def __init__(self):
        print("Person id: %d" % id(self))

''''

person = Person()
#First person object is instantiated, then multipled by 10, raising an error
person2 = Person() 
print(person2)

'''

#############identity equality and aliasing##############3
'''
No matter how I change the original list or any other lists they are going to b

Syntax:

x == y
x is y
'''




manta = {"company_name":"Manta"}
'''This is an alias below: you can see they refer to the same instantiated object'''
MANTA = manta
MANTA['employees'] = 50
NEWMANTA = MANTA
print(manta is MANTA)
print(MANTA is NEWMANTA)
print(manta is NEWMANTA)

'''This fails the test as there are two distinct objects even if they have the same contents
the objects do compare equal because of the special EQ magic method on dict class'''

alexander = {"firstname":"alexander","age":28}
alx = {"firstname":"alexander","age":28}
print(alexander == alx)
print(alexander is alx)


'''More practice on == vs is 
In summary use == when comparing the values and is when comparing identity. You rarely have to compare itentity but sometimes it's worth it to see if a variable is bound to none


'''
test_list = [x for x in range(1,10)]
identity_test_list = test_list
value_test_list = [x for x in range(1,10)]
value_test_list_false = [x for x in range(1,9)]
print("This should return true: %s" %(test_list is identity_test_list))
print("This should return false: %s" %(test_list is value_test_list))
print("this should return true: %s" %(test_list == value_test_list))
print("this should return false: %s" %(value_test_list == value_test_list_false))
