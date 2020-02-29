import random
import inquirer
from bs4 import BeautifulSoup
from HTMLParser import Parser
from WordExtractor import WordParser

# Start the gameplay
# Ask two types of different questions:
#	1. how often a word occurs in a chapter or in the whole book
#	2. what word occurs more often
#	-> use the Parser.getMostCommonWords function to extract the most common words
# 	-> create a new Parser function to extract the most common words from a chapter -> function takes the chapter number of 	does the rest automatically
# Create 5 random questions and ask the user the questions
# Check how many questions the users answered correctly and print the number of correct answers to the console

class PlayGame:
	def __init__(self, html, text, numberOfChapters):
		self.html = html
		self.text = text
		self.numberOfChapters = numberOfChapters
		self.userScore = 0
		self.round = 1

	def getRandomNumber(self):
		return random.randrange(2)

	def getRandomQuestionAssignment(self, correctAnswer, word1, word2, word3):
		number = random.randrange(0,4)
		if(number == 0):
			return [word1, correctAnswer, word2, word3]
		if(number == 2):
			return [word1, word2, correctAnswer, word3]
		if(number == 3):
			return [word1, word2, word3, correctAnswer]
		return [correctAnswer, word1, word2, word3]


	def getChapters(self, html):
		# get the toc and extract the number of chapters
		chapters = []
		tocElements = html.find_all("p", { "class": "toc" })
		for element in tocElements:
			if "CHAPTER" in element.text:
				chapters.append(element.text.replace("\n","",5).strip())
		return chapters

	def getMostCommonWordsInChapter(self, text, chapter):
		chapters = self.getChapters(self.html)
		chapter = text.split(chapters[chapter-1])[-1].split(chapters[chapter])[0]
		return WordParser(chapter).getMostCommonWords()

	def getGameQuestions(self, text, numberOfChapters):
		chapterNumber = random.randrange(numberOfChapters)
		mostCommonWordsInChapter = self.getMostCommonWordsInChapter(text, chapterNumber)
		if self.getRandomNumber() == 0:
			randNumber1 = random.randrange(2, 99)
			randNumber2 = random.randrange(2, 99)
			randNumber3 = random.randrange(2, 99)
			mostCommonWord = mostCommonWordsInChapter[0][0].lower()
			word2 = mostCommonWordsInChapter[randNumber1][0].lower()
			word3 = mostCommonWordsInChapter[randNumber2][0].lower()
			word4 = mostCommonWordsInChapter[randNumber3][0].lower()

			# Get the most common word from the chapter (chapterNumber)
			# Get the 3 other random words from that list
			# build a dict with the questions and the answer and return it
			return {
				"correctAnswer": mostCommonWord,
				"question": "What is the most common word in Chapter {}?".format(chapterNumber),
				"possibleAnswers": self.getRandomQuestionAssignment(mostCommonWord, word2, word3, word4)
			}
		else:
			# Get the number of occurrences from the chapter (chapterNumber)
			# Get another random word with its occurrences
			# build a dict with the questions and the answer and return it
			correctAnswer = mostCommonWordsInChapter[0][0].lower()
			randNumber1 = random.randrange(2, 99)
			possibleAnswers = []
			if random.randrange(2) == 0:
				possibleAnswers = [correctAnswer, mostCommonWordsInChapter[randNumber1][0].lower()]
			else:
				possibleAnswers = [mostCommonWordsInChapter[randNumber1][0].lower(), correctAnswer]
			return {
				"correctAnswer": correctAnswer,
				"possibleAnswers": possibleAnswers,
				"question": "What word occurs more often in chapter {}: {} or {}?".format(chapterNumber, mostCommonWordsInChapter[0][0].lower(), mostCommonWordsInChapter[randNumber1][0].lower())
			}

	def getFiveQuestions(self):
		return [
			self.getGameQuestions(self.text, self.numberOfChapters),
			self.getGameQuestions(self.text, self.numberOfChapters),
			self.getGameQuestions(self.text, self.numberOfChapters),
			self.getGameQuestions(self.text, self.numberOfChapters),
			self.getGameQuestions(self.text, self.numberOfChapters)
		]

	def printScore(self):
		if(self.userScore >= 3):
			print("Congratulations you are the winner!")
		else:
			print("Hmm, looks like you lost ... :(")
		print("You answered {} of 5 questions correctly.".format(self.userScore))
		print("\n\n")

	def start(self):
		print("Let's play!")
		rounds = self.getFiveQuestions()
		questions = []
		for r in rounds:
			questions.append(inquirer.List(self.round,
				message=r.get("question"),
				choices=r.get("possibleAnswers"),
			))
			self.round = self.round + 1
		answers = inquirer.prompt(questions)

		counter = 0
		for k,v in answers.items():
			if rounds[counter].get("correctAnswer") == v:
				self.userScore = self.userScore + 1
			counter = counter +1

		self.printScore()

