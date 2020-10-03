from games.models import Games 

from django.forms import ModelForm

class GamesForm(ModelForm):
    class Meta:
        model = Games
        fields = ['points', 'game_date']