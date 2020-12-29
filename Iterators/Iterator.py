import re
import reprlib


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = re.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator(Sentence):
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        try:
            word = self.words[self.index]
        except StopIteration:
            raise StopIteration()
        self.index += 1
        return word
