import time
import names
import random
import inquirer

from Setup import Init
from Game import PlayGame
from HTMLParser import Parser

# helper function which is used to play the first round
def playFirstRound(parser, setup):
	points = 0
	questions = [
		# ask for the author
		inquirer.List('round1',
			message="Who ist the author of moby dick?",
			choices=[names.get_full_name(gender="male"), parser.author, names.get_full_name(gender="male"), names.get_full_name(gender="male")],
		),
		# ask for the number of chapters
		inquirer.List('round2',
			message="How many chapters are there in moby dick?",
			choices=[94, 162, 108, parser.numberOfChapters],
		),
		# ask for the most common word in the whole book
		inquirer.List('round3',
			message="What ist the most common word in the book?",
			choices=[parser.mostCommonWord, parser.mostCommonWordsInBook[23][0], parser.mostCommonWordsInBook[12][0], parser.mostCommonWordsInBook[68][0]],
		),
		# ask how often the word whole occurs
		inquirer.List('round4',
			message="How often is the word 'whale' used in the book?",
			choices=[parser.mostCommonWordsInBook[0][1], parser.mostCommonWordsInBook[5][1], parser.mostCommonWordsInBook[12][1], parser.mostCommonWordsInBook[20][1]],
		),
		# ask what word occurs more often "captain" or "ship"
		inquirer.List('round5',
			message="What word occurs more often, '{}' or '{}'?".format(parser.mostCommonWordsInBook[1][0], parser.mostCommonWordsInBook[2][0]),
			choices=[parser.mostCommonWordsInBook[1][0], parser.mostCommonWordsInBook[4][0]]
		),
		]
	answers = inquirer.prompt(questions)
	correctAnswers = [
		parser.author,
		parser.numberOfChapters,
		parser.mostCommonWord,
		parser.mostCommonWordsInBook[0][1],
		parser.mostCommonWordsInBook[1][0]
	]
	# check how many answers are correct

	print("\n")
	print("Thanks. Let's see how you are doing.")
	time.sleep(2)
	print("\n")

	points = 0
	counter = 0
	for k,v in answers.items():
		if correctAnswers[counter] == v:
			points = points + 1
		counter = counter +1
	if(points >= 3):
		print("Congratulations you are the winner!")
	else:
		print("Hmm, looks like you need more practice ... :(")
	print("You answered {} of 5 questions correctly.".format(points))
	print("\n\n")
	time.sleep(2)
	setup.createSetupFile()
	return True


class Main:
	def __init__(self):
		self.test = "test"
		self.setup = Init()
		self.parser = False
		self.setupComplete = self.setup.checkSetup()
		self.HTMLExists = self.setup.checkHTML()

	def start(self):
		# check if the html exists. If not, create it
		if not self.HTMLExists:
			print("Before we start we need to prepare some things ...")
			self.setup.createHTMLFile() # create html file
			self.HTMLExists = True
			self.start() # call start method again to go through the whole process
		elif not self.setupComplete:
			if(not self.parser):
				self.parser = Parser()
			print("\n")
			print("First time playing, hmm?")
			print("Before we begin, let's go through some sample questions.")
			time.sleep(3)
			playFirstRound(self.parser, self.setup)
			self.setupComplete = True
			print("That's it for your first round. Ready for a real game?")
			time.sleep(2)
			print("\n")
			print("\n")
			self.start() # call start method again to go through the whole process
		else:
			if(not self.parser):
				self.parser = Parser()
			return PlayGame(self.parser.html, self.parser.text, self.parser.numberOfChapters).start()


def beginGame():
	print("Game is starting ...")
	g = Main()
	g.start()

beginGame()