import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .chatBot.chatBot import get_response 
from .chatBot.train_progress import train_bot_with_progress
import threading
import asyncio

class MyAsyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connected")
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print(f"Message from frontend: {text_data}")

        try:
            user_data = json.loads(text_data)
            user_message = user_data.get("message", "")

            bot_response = get_response(user_message)

            response_data = {
                "response": bot_response
            }

            await self.send(text_data=json.dumps(response_data))
            print("Sent to frontend:", json.dumps(response_data))



        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                "response": "Invalid message format!"
            }))
            print("Invalid JSON received")

    async def disconnect(self, close_code):
        print("WebSocket disconnected")


class TrainConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        print("🔌 Disconnected")

    async def receive(self, text_data):
        data = json.loads(text_data)

        if data.get("message") == "start_training":
            await self.send(text_data=json.dumps({
                "status": "Training started"
            }))

            def sync_callback(progress_data):
                
                asyncio.run(self.send_progress(progress_data))

            threading.Thread(target=train_bot_with_progress, args=(sync_callback,)).start()

    async def send_progress(self, progress_data):
        await self.send(text_data=json.dumps(progress_data))