
from nltk.tokenize import word_tokenize
import numpy as np

from nltk.stem import PorterStemmer
steamer = PorterStemmer();

#Tokenization of Sentence
def tokenization(sentence):
  return word_tokenize(sentence)

#Steming
def stemming(word):
  return steamer.stem(word.lower())


def bag_of_word(tokenized_sentence ,  array_all_word):
  tokenized_sentence = [ stemming(w) for w in tokenized_sentence] 
  
  bag = np.zeros(len(array_all_word) , dtype=np.float32) 
  for index , w in enumerate(array_all_word):
    if w in tokenized_sentence:
      bag[index] = 1.0
      
  return bag

