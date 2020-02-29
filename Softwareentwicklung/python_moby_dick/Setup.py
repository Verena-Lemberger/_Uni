from Scraper import MobyScraper

def getSetupFile():
	try:
		data = open("setup.txt","r")
		return True
	except:
		return False


def HTMLFileExists():
	try:
		data = open("mobydick.html","r")
		return True
	except:
		return False


class Init:
	def __init__(self):
		# check if the setup file exists. If yes, the user has already completed the setup
		self._setupComplete = getSetupFile()
		# check if the html file already exists
		self._mobyHTMLExists = HTMLFileExists()

	def createHTMLFile(self):
		MobyScraper().getMoby()

	def createSetupFile(self):
		f = open("setup.txt","w+")
		f.close()

	def checkSetup(self):
		return self._setupComplete

	def checkHTML(self):
		return self._mobyHTMLExists
