
from django.urls import path
from . import consumers

websocket_urlpatterns = [
  path("web-socket/chat/",consumers.MyAsyncConsumer.as_asgi()),
  path("ws/train/", consumers.TrainConsumer.as_asgi()),
]