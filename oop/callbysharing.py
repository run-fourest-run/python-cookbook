'''
Call by Sharing








'''

''





'''
a function may change any mutable object it is passed


'''



def callbysharing(a,f):
    a += f
    return a

a = [1,2,3,4,5]
f = (4,3,4)
print(callbysharing(a,f))
a = 1
f = 2
print(callbysharing(a,f))


def typeenforced(x,testlist=[]):
    testlist.append(x)
    testlist.sort()
    return testlist

def nottypeenforced(x,testlist):
    testlist.append(x)
    testlist.sort()
    return testlist

testlist = [50,40]
x = 60
print("you can see this is type enforced {}".format(typeenforced(x,testlist)))
testlist = 5
x = 50
print("you can see this is not type enforced {}".format(typeenforced(x,testlist)))
