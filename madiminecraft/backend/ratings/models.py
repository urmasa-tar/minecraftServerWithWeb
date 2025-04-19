from django.db import models
from django.conf import settings

class PlayerStats(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    play_time = models.IntegerField(default=0)  # в минутах
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    last_online = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} stats"