
import json #json load garna lai use gareko

from nltk_utils import tokenization , stemming , bag_of_word

import numpy as np

import torch.nn as nn 
from torch.utils.data import Dataset , DataLoader
import torch

from model import NeuralNetwork

with open("intents.json","r") as f:
  intents = json.load(f)

'''
json lai load garesi we get "intents" as 
{
  "intents" : [
    {
    "tags" : _______,
    "patterns" : [],
    "responses" : [],
    "context" : []
    }
  ]
}


so intents["intents"] le -> List dincha ani Tesma For Loop Lagauna Milcha
& Each Item is Dictionary

'''

all_words = []
tags = []
xy = []  #later it holds both our patterns and then the text

for intent in intents["intents"]:
  tag = intent.get("tag")
  tags.append(tag)
  
  for pattern in intent["patterns"]:
    #pattern is List
    w = tokenization(pattern)
    all_words.extend(w) #extend le duita array lai merge garcha
    #append le array ma arko array last ma halcha
    #so yo bela expand use gareko
    
    xy.append((w , tag)) #pattern and its corresponding tag
    

ignore_words = ['?','!','.',',']
# print(all_words)

all_words = [ stemming(w) for w in all_words if w not in ignore_words]
#esle sabai words lai steam garcha and ignore word lai bayek ko words haru dincha

all_words = sorted(all_words) #esle sorted garcha
#unique pauna lai 
all_words = set(all_words) #we get unique sorted array -> remove duplicated words
# print(all_words)

tags = sorted(set(tags))
# print(tags)

X_train = []
y_train = []

for (pattern_sentence , tag) in xy:
  bag = bag_of_word(pattern_sentence , all_words)
  X_train.append(bag)
  
  label = tags.index(tag)
  y_train.append(label) #CrossEntropyLoss
  
X_train = np.array(X_train)
y_train = np.array(y_train)


class ChatDataSet(Dataset):
  def __init__(self):
    self.n_samples = len(X_train)
    self.x_data =  X_train
    self.y_data = y_train
    
  def __getitem__(self , index):
    return self.x_data[index] , self.y_data[index]
  
  def __len__(self):
    return self.n_samples
  
#Hyperparameters
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(X_train[0]) #X_train[0] le 1st bag of words dincha
learning_rate = 0.001
num_of_epochs = 1000
  
dataset = ChatDataSet() #object
train_loader = DataLoader(dataset=dataset , batch_size=batch_size, shuffle=True , num_workers=0)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = NeuralNetwork(input_size , hidden_size , output_size).to(device)


#Loss & Optimizer

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate) 

for epoch in range(num_of_epochs):
  for (words , labels) in train_loader:
    words = words.to(device)
    labels = labels.to(device)
    
    
    #Forward
    outputs = model(words)
    loss = criterion(outputs , labels)
    
    
    #Backward & Optimizer Step
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
  if (epoch + 1) % 100 == 0:
    print(f"Epoch {epoch + 1}/{num_of_epochs} , loss={loss.item():.4f}")

print(f"Final Loss , loss={loss.item():.4f}")


data = {
  "model_state" : model.state_dict(),
  "input_size" : input_size,
  "output_size" : output_size,
  "hidden_size" : hidden_size,
  "all_words" : all_words,
  "tags" : tags
}


FILE = "data.pth"
torch.save(data , FILE)
print(f"Training Completed . File Saved to {FILE}")