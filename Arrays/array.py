from array import array #1
from random import random




'''
if the list only contains numbers than an array.array is more efficient
* It supports all mutable sequence operations (.pop,.insert,.extend)
* Additional methods for fast loading and saving such as .frombyte and .tofile
'''

floats = array('d',(random() for t in range(10**7)))
fp = open('floats.bin','wb')
floats.tofile(fp)
fp.close()
print(floats[-1])
floats2 = array('d')
fp = open('floats.bin','rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])


floats = array('d',(random() for t in range(10**3)))
sorted_floats = sorted(floats)
for x in sorted_floats:
    print(x)