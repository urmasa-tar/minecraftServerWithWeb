from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=15)
    port = models.IntegerField(default=25565)
    password = models.CharField(max_length=100, blank=True, null=True)
    is_online = models.BooleanField(default=False)
    last_checked = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name