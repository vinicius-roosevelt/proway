from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.db import models

from games.utils import *

class Games(models.Model):
    points = models.PositiveIntegerField(verbose_name='Quantidade de pontos')
    game_date = models.DateField(verbose_name='Data do jogo', blank=True, null=True)

    def __str__(self):
        return 'Jogo n. %s ' % (self.id)

    def get_absolute_url(self):
        return reverse('games:update-game', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('games:delete-game', kwargs={'pk': self.pk})
    
    def get_update_url(self):
        return reverse('games:update-game', kwargs={'pk': self.pk})

    def get_max_season(self):
        value = calculate_max_season(self, Games.objects.all().order_by('game_date', 'id'))
        return value

    def get_min_season(self):
        value = calculate_min_season(self, Games.objects.all().order_by('game_date', 'id'))
        return value
    
    def get_is_min_break(self):
        value = is_min_break(self, Games.objects.all().order_by('game_date', 'id'))
        return value

    def get_is_max_break(self):
        value = is_max_break(self, Games.objects.all().order_by('game_date', 'id'))
        return value

    def get_max_breaks_amount(self):
        value = get_break_max_amount(self, Games.objects.all().order_by('game_date', 'id'))
        return value

    def get_min_breaks_amount(self):
        value = get_break_min_amount(self, Games.objects.all().order_by('game_date', 'id'))
        return value
