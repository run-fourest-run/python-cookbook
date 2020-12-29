'''


Iterable:
* any object from which  the iter built-in function can obtain an iterator: Objects implementing an __iter__ method returning an iterator are iterable
* sequences are always iterable
* as are objects using the __getitem__ method that takes a zero based index
* Python obtains iterators from iterables

Iterator:
* Any object that implements the __next__ no arguement method that returns the next item in a series or raises
StopIteration when there is no more items. Python iterators implement __iter__ method so they are iterable as well.

'''



str = 'test'

for letter in str:
    print(letter)




'''mimicking the above for loop machinery with a while look is .... ugly'''
it = iter(str) #builds an iterator from the iterable
while True:
    try:
        print(next(it))#repeatedly call next
    except StopIteration: #raisis StopIteration when there are no further items
        del it # releases reference to it
        break #exit the loop

'''
standard interface for an iterator has two methods: __next__ & __iter__
* __next__ : Returns the next availble item and raises StopIteration exception when there are no further items
* __iter__: returns self; this allows the iterators to used where iterables are expected.
'''