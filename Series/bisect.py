import bisect
import sys


# Bisect module helps with Binary Searches
# two main functions bisect and insort
# input is a sorted sequence


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    t = bisect.bisect(breakpoints,score)
    return grades[t]




print([grade(score) for score in [42,64,100,30]])

