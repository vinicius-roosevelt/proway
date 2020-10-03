from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
from django.db.models import Avg, Max, Min

from games.models import Games
from games.forms import GamesForm
from games.utils import *

class Home_view(ListView):

    template_name='home.html'
    model = Games
    queryset = Games.objects.all().order_by('-game_date','-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['min_season'] = self.queryset.aggregate(Min('points'))['points__min']
        context['max_season'] = self.queryset.aggregate(Max('points'))['points__max']
        context['break_max_amount'] = get_break_max_amount(None, Games.objects.all().order_by('game_date','id'))
        context['break_min_amount'] = get_break_min_amount(None, Games.objects.all().order_by('game_date','id'))
        return context


class GamesCreate(CreateView):
    model = Games
    template_name = 'games_form.html'
    form_class = GamesForm
    success_url = reverse_lazy('games:list-games')


class UpdateGames(UpdateView):
    model = Games
    template_name = 'games_form.html'
    form_class = GamesForm
    success_url = reverse_lazy('games:list-games')

class GamesDelete(DeleteView):
    model = Games
    success_url = reverse_lazy('games:list-games')
