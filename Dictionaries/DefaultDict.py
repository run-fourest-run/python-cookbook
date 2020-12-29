import collections
import sys
import re


names = ['Alexander','Thomas','James','Charlie']
values = [x+1 for x in range(len(names))]
test_string = 'this is my test string'
position = 10

def zipped_dict():
    zipped_dict = dict(zip(names,values))
    for key,value in zipped_dict.items():
        print(key,value)





def enumerate_string(test_string,position):
    for index,value in enumerate(test_string):
        print(index,value)






WORD_RE = re.compile('\w+')

index = collections.defaultdict(list)
with open(sys.argv[-1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp,start=1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no,column_no)
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word,index[word])



