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


# initial number to start a chain
num = '90052'

# relative path to the file, witch should be opened next
rel_path = 'data_p6/{}.txt'.format(num)

# opens a file from relative path and reads the content
with open(rel_path, 'r') as f:
    text = f.read()

# extract num from a text using the find utility function
num = (find('Next nothing is ([0-9]{1,7})', text))

# prints the num on the screen
print('Next num to put into a filename is: {}'.format(num))
