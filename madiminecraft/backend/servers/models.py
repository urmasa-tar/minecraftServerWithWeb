from django.db import models
# Удалите ранний импорт get_user_model()

class Server(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=15)
    port = models.IntegerField(default=25565)
    password = models.CharField(max_length=100, blank=True, null=True)
    is_online = models.BooleanField(default=False)
    last_checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name