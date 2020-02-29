import random
from bs4 import BeautifulSoup
from WordExtractor import WordParser

# Ask two types of different questions:
#	1. how often a word occurs in a chapter or in the whole book
#	2. what word occurs more often
#	-> use the Parser.getMostCommonWords function to extract the most common words
# 	-> create a new Parser function to extract the most common words from a chapter -> function takes the chapter number of 	does the rest automatically
# Create 5 random questions and ask the user the questions
# Check how many questions the users answered correctly
# Ask the user if she want's to play again
# If yes, call start() function again. If no, quit the game

def getRandomNumber():
	return random.randrange(2)

def getRandomQuestionAssignment(correctAnswer, word1, word2, word3):
	number = random.randrange(0,4)
	if(number == 0):
		return [word1, correctAnswer, word2, word3]
	if(number == 2):
		return [word1, word2, correctAnswer, word3]
	if(number == 3):
		return [word1, word2, word3, correctAnswer]
	return [correctAnswer, word1, word2, word3]


def getChapters(html):
	# get the toc and extract the number of chapters
	chapters = []
	tocElements = html.find_all("p", { "class": "toc" })
	for element in tocElements:
		if "CHAPTER" in element.text:
			chapters.append(element.text.replace("\n","",5).strip())
	return chapters

def getMostCommonWordsInChapter(textSoup, chapter):
	chapter = textSoup.split(chapters[chapter-1])[-1].split(chapters[chapter])[0]
	return WordParser(chapter).getMostCommonWords()

def getGameQuestions(textSoup, numberOfChapters):
	chapterNumber = random.randrange(numberOfChapters)
	mostCommonWordsInChapter = getMostCommonWordsInChapter(textSoup, chapterNumber)
	if getRandomNumber() == 0:
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
			"possibleAnswers": getRandomQuestionAssignment(mostCommonWord, word2, word3, word4)
		}
	else:
		# Get the number of occurrences from the chapter (chapterNumber)
		# Get another random word with its occurrences
		# build a dict with the questions and the answer and return it
		correctAnswer = mostCommonWordsInChapter[0][1]
		randNumber1 = random.randrange(2, 99)
		possibleAnswers = []
		if random.randrange(2) == 0:
			possibleAnswers = [correctAnswer, mostCommonWordsInChapter[randNumber1][1]]
		else:
			possibleAnswers = [mostCommonWordsInChapter[randNumber1][1], correctAnswer]
		return {
			"correctAnswer": correctAnswer,
			"possibleAnswers": possibleAnswers,
			"question": "What word occurs more often in chapter {}: {} or {}?".format(chapterNumber, mostCommonWordsInChapter[0][0], mostCommonWordsInChapter[randNumber1][0])
		}

def getFiveQuestions(textSoup, numberOfChapters):
	return [
		getGameQuestions(textSoup, numberOfChapters),
		getGameQuestions(textSoup, numberOfChapters),
		getGameQuestions(textSoup, numberOfChapters),
		getGameQuestions(textSoup, numberOfChapters),
		getGameQuestions(textSoup, numberOfChapters)
	]

# get the data
data = open("mobydick.html","r")
# load data into bs4 and get the text
htmlSoup = BeautifulSoup(data, "html.parser")
textSoup = htmlSoup.text

chapters = getChapters(htmlSoup)
mostCommonWordsInChapter = getMostCommonWordsInChapter(textSoup, 50)

# replace 100 with the real number of chapters
numberOfChapters = 100
print(getFiveQuestions(textSoup, numberOfChapters))


