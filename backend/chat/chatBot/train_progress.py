import time

def train_bot_with_progress(callback):
    for i in range(1, 101): 
        time.sleep(0.1)  
        callback({
            'percent': i,
            'status': f'Training in progress: {i}%' 
        })
