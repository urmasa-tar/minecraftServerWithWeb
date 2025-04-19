from django.db import models
from django.contrib.auth.models import User

class PlayerStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    play_time = models.IntegerField(default=0)  # в минутах
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    last_online = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} stats"

    @property
    def kd_ratio(self):
        if self.deaths > 0:
            return self.kills / self.deaths
        return self.kills