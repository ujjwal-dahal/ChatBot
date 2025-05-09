
import random 
import json 
import torch 
from model import NeuralNetwork
from nltk_utils import bag_of_word , tokenization

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


with open("intents.json", "r") as f:
  intents = json.load(f)
  
FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNetwork(input_size , hidden_size , output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "BRIGHTBOT"
print("Let's Chat! Type 'quite' to Exit")

while True:
    sentence = input("You: ")
    if sentence.lower() == "quit":
        break

    sentence = tokenization(sentence)
    X = bag_of_word(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).float().to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probability = torch.softmax(output, dim=1)
    prob = probability[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: I do not understand...")

  