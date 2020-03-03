# Moby Dick Web-Scraper and Command Line Game

## What is it?
This is a python web-scraper and command line game. It scrapes the complete moby dick book from "https://www.gutenberg.org/files/2701/2701-h/2701-h.htm" and extracts the most common words from each chapter. You then get questions about the data we extracted.

The types of questions can either be what the most common word in a chapter is, or which word (out of 2 possible choices) occurs more often in a specific chapter.

Your job is to answer at least 3 out of 5 questions correctly to win the game.



## Setup & Installation

To play the game you must have at least Python 3 (we used version 3.7) installed. Additionally you have to do the following steps:

1. run "pip3 install --user -U nltk"
2. run "python -m nltk.downloader all" to download the necessary nltk packages (this may take a while)
3. install all the other necessary dependencies
	- pip3 install requests
	- pip3 install inquirer
	- pip3 install beautifulsoup4
	- pip3 install Counter
	- pip3 install names
	- pip3 install stop_words
4. run "python main.py" to start the game

## Team Members
- Sebastian Schäffer
- Sascha Metzger

