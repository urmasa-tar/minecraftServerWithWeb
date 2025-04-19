from django.shortcuts import render
from django.contrib.auth.models import User
from .models import PlayerStats

def player_ratings(request):
    # Получаем статистику игроков, сортируем по убийствам (kills)
    stats = PlayerStats.objects.select_related('user').all().order_by('-kills')
    return render(request, 'ratings/ratings.html', {'stats': stats})