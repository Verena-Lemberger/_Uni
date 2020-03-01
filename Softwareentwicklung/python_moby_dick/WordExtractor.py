import string
from collections import Counter
from nltk.corpus import stopwords
from stop_words import get_stop_words
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

class WordParser:

	def __init__(self, text):
		self.text = text

	def getMostCommonWords(self):
		porter = PorterStemmer()
		stopWords = stopwords.words('english')

		# add custom stopwords
		customStopWords = ["like", "upon", "would", "though", "long", "sill", "great", "said", "must", "seemed", "last", "look", "chapter", "thing", "still", "come", "white", "thou", "stubb"]
		for word in customStopWords:
			stopWords.append(word)

		# split text into single words
		tokens = word_tokenize(self.text)

		# convert to lower case
		words = [w.lower() for w in tokens]

		# remove punctuation from each word
		t = str.maketrans('', '', string.punctuation)
		words = [w.translate(t).lower() for w in tokens]

		# remove tokens that are not alphabetic
		words = [word for word in words if word.isalpha()]

		# remove stopwords
		words = [w for w in words if not w in stopWords]

		# make sure the remaining words have at least 3 letter
		words = [w for w in words if len(w) > 3]

		return Counter(words).most_common(100)