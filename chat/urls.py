from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'), #se pasara la variable room por el urls
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),#url dinamica para que aparezcan los mensajes refrescados en tiempo real en el room
]