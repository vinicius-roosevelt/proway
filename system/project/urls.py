from django.contrib import admin
from django.urls import path, include

app_name = 'project'
urlpatterns = [
    path('', include('games.urls')),
    path('admin/', admin.site.urls),
]
