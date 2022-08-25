from django.urls import path

from main.views import BoardListApiView, BoardDetailApiView, \
    BoardDataDetailApiView

app_name = 'main'

urlpatterns = [
    path('boards/', BoardListApiView.as_view(), name='boards'),
    path('boards/<int:pk>/', BoardDetailApiView.as_view(),
         name='board_detail'),
    path('boards/<int:pk>/view/', BoardDataDetailApiView.as_view(),
         name='boards_list_view'),
]
