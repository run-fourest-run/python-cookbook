'''
Tuples remain immutable in kind of an interesting way. The references to the objects they contain can not be changed. But the underlying object that the variable has been
assigned too can change.


'''
x = 10

t1 = (1,2,[30,50])
print("this is t1: %s" % (t1,))
t2 = (1,2,[30,50])
print("this is t2:  %s" % (t2,))
print("equality operator will return true: %s" % (t1 == t2))
t2[-1].append(x)
print("this is t2 after we sliced it: %s" % (t2,))
print("equality operator will return False: %s" % (t1 == t2))
t3 = t2
print("this is t3: %s" % (t3,))
t3[-1].append(x)
print("this is t3: %s" % (t3,))
print("equality operator will return false: %s" % (t1 == t3))


#### Let's copy a list but make two sepearte objects


test_list = [1,2,3,4,5]
copy_list = list(test_list)
print("Is Testlist and copy list equal: %s" % (test_list==copy_list))
print("Is Testlist and copy list identical (Share the same identity): %s" % (test_list is copy_list))