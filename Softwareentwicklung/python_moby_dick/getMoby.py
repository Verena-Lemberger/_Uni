import requests
from bs4 import BeautifulSoup

# get the data
print("starting request ...")
data = requests.get("https://www.gutenberg.org/files/2701/2701-h/2701-h.htm")

# load data into bs4
print("fetched data - start processing ...")
soup = BeautifulSoup(data.text, 'html.parser')

# create a new json file and save the soup response
f = open("mobydick.html","w+")
f.write(str(soup))
f.close()