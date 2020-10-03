from django.contrib import admin
from django.urls import path, include
from games import views

app_name = 'games'
urlpatterns = [
    path('', views.Home_view.as_view(), name='list-games'),
    path('adicionar', views.GamesCreate.as_view(), name='create-game'),
    path('excluir/<int:pk>', views.GamesDelete.as_view(), name='delete-game'),
    path('atualizar/<int:pk>', views.UpdateGames.as_view(), name='update-game'),
]
