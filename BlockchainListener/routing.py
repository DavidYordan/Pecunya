from django.urls import re_path

from BlockchainListener import consumers

websocket_urlpatterns = [
    re_path(r'ws/blockchain/$', consumers.BlockchainConsumer.as_asgi()),
]