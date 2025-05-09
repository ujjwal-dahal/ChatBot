
import nltk
from nltk.tokenize import word_tokenize
import numpy as np

from nltk.stem import PorterStemmer
steamer = PorterStemmer();


#Ek palta download bhaesi no need
# nltk.download('punkt')
# nltk.download('punkt_tab')

#Tokenization of Sentence
def tokenization(sentence):
  return word_tokenize(sentence)

#Steming
def stemming(word):
  return steamer.stem(word.lower())


def bag_of_word(tokenized_sentence ,  array_all_word):
  tokenized_sentence = [ stemming(w) for w in tokenized_sentence] #stemming gareko
  
  bag = np.zeros(len(array_all_word) , dtype=np.float32) #jati ota words chan teti ko length ko 0 wala array
  for index , w in enumerate(array_all_word):
    if w in tokenized_sentence:
      bag[index] = 1.0
      
  return bag


# sentence = ["hello" , "how" , "are" , "you"]
# words = ["hi","hello","I","you","bye","thank","cool"] 
# bag = bag_of_word(sentence , words)
# print(bag)
# #sentence ko each word chahi words ma khojcha and tai anusar cha bhane 1 nabhai 0
   

'''
enumerate() function le iterable variable as a parameter lincha
ani Esle chai Tuple return garcha having index & value in each tuple

exmple : newList = ["a" , "b" , "c"]
enumerate(newList) -> [
  (0 , "a") , (1 , "b") , (2 , "c")
]

'''


# #Check 
# sentence = "Ram is Running. He is Good Runner"
# print(f"\nOriginal Sentence : {sentence}\n")

# tokenized_sentence = tokenization(sentence)
# print(f"Tokenized Sentence : {tokenized_sentence}\n")

# #Tokenization garesi Each word lai Stemming garne ho

# # for word in tokenized_sentence:
# #   stemmed_word = stemming(word)
# #   print(f"After Stemming : {stemmed_word}\n")

# #Stemming using List Comprehension

# stemmed_list = [ stemming(word) for word in tokenized_sentence]
# print(stemmed_list)