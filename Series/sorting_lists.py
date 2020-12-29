list1 = [x for x in range(10)]
list2 = ['alexander','paige','bruce']


# Returns a new list

new_list = sorted(list1)

new_list_sortbykey = sorted(list1, key=len)

new_list_reversed = sorted(list1,reverse=True)



# sorts the list in place

list1.sort()

# Reverse list in place

list1.reverse()