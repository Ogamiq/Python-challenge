#!usr/bin/env python
#This program operates on the data inside the folder data_p6

import re

# utility function operating on regular expressions suitable for the task
def find(pat, text):
    match = re.search(pat, text)
    if match:
        return match.group(1)
    else:
        raise ValueError("Function 'find' didn't find num in text")


#TODO: make a loop to access the files

counter = 1
num = '90052' #initial number to start the block chain
while(counter < 910):
    rel_path = 'data_p6/{}.txt'.format(num)
    with open(rel_path, 'r') as f:
        text = f.read()
    num = (find('Next nothing is ([0-9]{1,7})', text))
    print('Iteration: {}  Next num to put into a filename is: {}'.format(counter,num))
    counter += 1


