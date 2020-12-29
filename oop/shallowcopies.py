'''Using a constructor or copying any sort of container generally results in a 'shallow copy'
What this means is the outer container is copied but the copy is filled with references to the same items help by the original container
This can lead to problems if the items are mutable
'''

'''
test_list = [1,2,3,4,[5,"test"]]
print("this is the test list: %s" %(test_list))
copy_list = list(test_list)
print("this is the copy list: %s" %(copy_list))
print("They pass the equality test: %s" % (test_list == copy_list))
test_list.append(100)
test_list[4].remove('test')
print("this is the new changed test_list: %s" %(test_list))

print("this is the test list: %s" %(test_list))
print("this is the copy list: %s" %(copy_list))
print("They pass the equality test: %s" % (test_list == copy_list))
'''

'''
test_list = [[1,2,3],5,(200,300)]
print("this is the test list: %s" %(test_list))
copy_list  = list(test_list)
print("this is the copy list: %s" %(copy_list))
print("They pass the equality test: %s" % (test_list == copy_list))
test_list.append(50)
print("this is the test list: %s" %(test_list))
print("this is the copy list: %s" %(copy_list))
print("they should be equal: %s" % (test_list == copy_list))
test_list[0].remove(3)
print("this is the test list: %s" %(test_list))
print("this is the copy list: %s" %(copy_list))
print("they should not be equal: %s" % (test_list == copy_list))
copy_list[0] += [1,2,3,4]
print("this is the test list: %s" %(test_list))
print("this is the copy list: %s" %(copy_list))'''




test_list = [[1,2,3],'test',4,(1,2,3)]
copy_list = list(test_list)
print("these will pass equality: %s" % (test_list == copy_list))
print("this is the test list: %s" %(test_list))
print("this is the copy list: %s" %(copy_list))
test_list[0].remove(1)

print("this is the test list: %s" %(test_list))
print("this is the copy list: %s" %(copy_list))
print("these will pass equality: %s" % (test_list == copy_list))
test_list[0] += [50,70]
print("this is the test list: %s" %(test_list))
print("this is the copy list: %s" %(copy_list))
print("these will pass equality: %s" % (test_list == copy_list))
test_list[3] += (50,70)
print("this is the copy list: %s" %(copy_list))
print("this is the test list: %s" %(test_list))
print("these will pass equality: %s" % (test_list == copy_list))

print("this is the copy list: %s" %(copy_list))
print("this is the test list: %s" %(test_list))
print("these will pass equality: %s" % (test_list == copy_list))