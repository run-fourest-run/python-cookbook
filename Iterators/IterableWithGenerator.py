import re
import reprlib
'''
instead of creating two distinct Classes for the iterator protocol: Iterator & Iterable -
you can use a generator function in it's place
'''

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)'.format(reprlib.repr(self.text))

    def __iter__(self):
        for word in self.words:
            yield word
        return

'''
notice in the __iter__ dunder method instead of calling an Iterator class we are using a generator function
yielding the word one at a time. I don't need the return on the bottom line -> the iteration can just 'fall through'

'''

test_iterable = Sentence('this is my sentence')

for x in test_iterable:
    print(x)