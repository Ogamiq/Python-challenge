import requests
from bs4 import BeautifulSoup, Comment
from collections import Counter

#get website content and assign it to soup object
url = ("http://www.pythonchallenge.com/pc/def/ocr.html")
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')

#find comments inside the content of soup object
comments = soup.find_all(string = lambda text:isinstance(text,Comment))

#extract data relevant for further processing
data = comments[1]

#create dictionary of chars and their frequencies using counter
counter = Counter(data)

#construct the message from chars who occurred only once in the data
message = []
for key, value in counter.items():
    if value == 1:
        message.append(key)
print(''.join(message))

# after the message is printed, guess the password
#equality













