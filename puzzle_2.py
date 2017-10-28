import requests
from bs4 import BeautifulSoup, Comment

#get website content and assign it to soup object
url = ("http://www.pythonchallenge.com/pc/def/ocr.html")
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')


#find comments inside the content
comments = soup.find_all(string = lambda text:isinstance(text,Comment))


#extract data relevant for further processing
data = comments[1]


#test if the data is correct
print("First 30 chars:{}".format(data[:30]))
print("Last 30 chars:{}".format(data[-31:]))












