#!usr/bin/env python

#initial number to start a chain
num = '90052'

#relative path to the file, witch should be opened next
rel_path = 'data_p6/{}.txt'.format(num)


#TODO: using relative file path open a file and display to the console the text inside of it

with open(rel_path,'r') as file:
    text = file.read()
    print(text)
