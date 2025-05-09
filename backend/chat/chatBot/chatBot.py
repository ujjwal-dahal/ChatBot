import random
import json
import torch
from .model import NeuralNetwork
from .nltk_utils import bag_of_word, tokenization
import os
from django.conf import settings


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


if not settings.configured:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")


intents_path = os.path.join(settings.BASE_DIR, "intents.json")
model_path = os.path.join(settings.BASE_DIR, "trainedModel.pth")


with open(intents_path, "r", encoding="ISO-8859-1") as f:
    intents = json.load(f)


data = torch.load(model_path)


input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]


model = NeuralNetwork(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


def get_response(user_message):
   
    sentence_tokens = tokenization(user_message)
    X = bag_of_word(sentence_tokens, all_words)
    X = X.reshape(1, -1) 
    X = torch.from_numpy(X).float().to(device)

    
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    
    probability = torch.softmax(output, dim=1)
    prob = probability[0][predicted.item()]

 
    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    else:
        return "Sorry I can't understand"

