from django.urls import path

from main import consumers

websocket_urlpatterns = [
    path('ws/boards/<int:pk>/view/',
         consumers.BoardDataConsumerDetail.as_asgi()),
]
