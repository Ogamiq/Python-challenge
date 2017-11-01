import requests
import re
from bs4 import BeautifulSoup



def find(pat,text):
    match = re.search(pat,text)
    if match:
        return match.group()


num = '12345' # initial value of nothing to start the chain

counter = 0

while counter <= 400:

    url = ("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(num))
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    text = str(soup.findAll(text=True))
    num = (find('[0-9]{1,7}',text))
    print("Iteration {}: next num to put in the url is: {} ".format(counter,num))
    counter += 1
