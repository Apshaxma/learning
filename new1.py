import nltk 
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

text = "This is a Program in NLTK"

tagged_words = pos_tag(word_tokenize(text))

print(tagged_words)