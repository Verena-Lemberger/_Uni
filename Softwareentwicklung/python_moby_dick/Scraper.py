import requests
from bs4 import BeautifulSoup

class MobyScraper:

	def getMoby(self):
		# get the data
		print("You didn't download the book moby dick yet. We need to do this before we begin.")
		print("Starting download ...")
		data = requests.get("https://www.gutenberg.org/files/2701/2701-h/2701-h.htm")

		# load data into bs4
		print("fetched data - start processing the html ...")
		soup = BeautifulSoup(data.text, 'html.parser')

		# create a new json file and save the soup response
		f = open("mobydick.html","w+")
		f.write(str(soup))
		f.close()

		print("Setup complete!")
