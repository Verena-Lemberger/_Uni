from bs4 import BeautifulSoup

# get the data
data = f = open("mobydick.html","r")

# load data into bs4
soup = BeautifulSoup(data, 'html.parser')

# get the toc
toc = soup.find('p', { 'class': 'toc' })

print(toc)
