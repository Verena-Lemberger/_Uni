from bs4 import BeautifulSoup
from WordExtractor import WordParser


def getHTML():
	try:
		# get the data
		data = open("mobydick.html","r")
		# load data into bs4
		htmlSoup = BeautifulSoup(data, "html.parser")
		# return the html
		return htmlSoup
	except:
		pass


class Parser:
	def __init__(self):
		self.html = getHTML()
		self.text = self.html.text
		self.author = self.getAuthor()
		self.numberOfChapters = self.getNumberOfChapters()
		self.mostCommonWordsInBook = WordParser(self.html.text).getMostCommonWords()
		self.mostCommonWord = self.mostCommonWordsInBook[0][0]


	def getNumberOfChapters(self):
		# get the toc and extract the number of chapters
		numberOfChapters = 0
		tocElements = self.html.find_all("p", { "class": "toc" })
		for element in tocElements:
			if "CHAPTER" in element.text:
				numberOfChapters = numberOfChapters + 1
		return numberOfChapters


	def getAuthor(self):
		# fetch the author of moby dick
		author = self.html.find("h2").text.replace("By", "").strip()
		return author



