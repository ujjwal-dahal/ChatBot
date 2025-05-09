import json
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn

from .nltk_utils import tokenization, stemming, bag_of_word
from .model import NeuralNetwork  


# train.py
def train_bot(user_given_epoch):
    import os
    from django.conf import settings
    
   
    if not settings.configured:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

    INTENTS_PATH = os.path.join(settings.BASE_DIR, "intents.json")
    MODEL_PATH = os.path.join(settings.BASE_DIR, "trainedModel.pth")

    with open(INTENTS_PATH, "r") as f:
        intents = json.load(f)

    all_words = []
    tags = []
    xy = []

    
    for intent in intents["intents"]:
        tag = intent.get("tag")
        tags.append(tag)

        for pattern in intent["patterns"]:
            w = tokenization(pattern)  
            all_words.extend(w)  
            xy.append((w, tag))  

    ignore_words = ['?', '!', '.', ',']

    
    all_words = [stemming(w) for w in all_words if w not in ignore_words]
    all_words = sorted(set(all_words))  
    tags = sorted(set(tags))  

    
    X_train = []
    y_train = []

    for (pattern_sentence, tag) in xy:
        bag = bag_of_word(pattern_sentence, all_words)  
        X_train.append(bag)
        label = tags.index(tag)  
        y_train.append(label)

    X_train = np.array(X_train)
    y_train = np.array(y_train)

   
    class ChatDataSet(Dataset):
        def __init__(self):
            self.n_samples = len(X_train)
            self.x_data = X_train
            self.y_data = y_train

        def __getitem__(self, index):
            return self.x_data[index], self.y_data[index]

        def __len__(self):
            return self.n_samples

    
    batch_size = 8
    hidden_size = 8
    output_size = len(tags)
    input_size = len(X_train[0])  
    learning_rate = 0.001
    num_of_epochs = user_given_epoch

    
    dataset = ChatDataSet()  
    train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = NeuralNetwork(input_size, hidden_size, output_size).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

   
    for epoch in range(num_of_epochs):
        for (words, labels) in train_loader:
            words = words.to(device)
            labels = labels.to(device)

           
            outputs = model(words)
            loss = criterion(outputs, labels)

           
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

       
        if (epoch + 1) % 100 == 0:
            print(f"Epoch {epoch + 1}/{num_of_epochs}, Loss: {loss.item():.4f}")

    
    print(f"Final Loss: {loss.item():.4f}")

    
    data = {
        "model_state": model.state_dict(),
        "input_size": input_size,
        "output_size": output_size,
        "hidden_size": hidden_size,
        "all_words": all_words,
        "tags": tags
    }

   
    torch.save(data, MODEL_PATH)
    print(f" Model saved to: {MODEL_PATH}")
    
    
