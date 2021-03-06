import requests
import re
from bs4 import BeautifulSoup


def find(pat,text):
    match = re.search(pat,text)
    if match:
        return match.group(1)


num = '12345' # initial value of nothing to start the chain
counter = 0

while counter <= 400:

    url = ("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(num))
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    text = str(soup.findAll(text=True))

    #according to the clue from iteration 84 I am supposed to divide
    #'number to put in the next url' by two to get properly to iteration 85
    #all other numbers should be passed as they are
    if counter == 84:
         num = str(int((find('and the next nothing is ([0-9]{1,7})',text)))/2)
    else:
        num = (find('and the next nothing is ([0-9]{1,7})',text))

    print("Iteration {}: next num to put in the url is: {} ".format(counter,num))
    counter += 1

#Puzzle 4 solved!! Without any external help. Took me 1 hour and 15 minutes to program it, but
#I've been thinking about this task yesterday.

#The answer is found at iteration: 248, number 66831 ---> peak.html
