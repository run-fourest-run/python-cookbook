import array

# Why use a generator expression?
#
# A Generator expression saves memory. You could use a listcomp to intialize a sequence
#
# it saves memory by yielding one item at a time using the iterator protocol instead of building an
# entire list to be fed into another constructor
#
# Generator Methods use the same syntax as list comprehensions but are enclosed in ( )



# Example 1

symbols = '$¢£¥€¤'
tuple_example = tuple(ord(symbol) for symbol in symbols)
print(tuple_example)
testvalues = [1,2,3,4,5,6]

#Example 2
#array constructor takes two arguements so you need to double enclose the second argument

array_example = array.array('I',(ord(symbol) for symbol in symbols))

node_name = ['/SSIS/Scdmerge','/SSIS/SCDsource' ]
node_parent_name = ['/test', '/test1','/test2','/test1']

for row in ('%s:%s' % (x,y) for x in node_parent_name for y in node_name):
    print(row)