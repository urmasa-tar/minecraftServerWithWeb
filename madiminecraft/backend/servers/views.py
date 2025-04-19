from django.shortcuts import render
from .models import Server

def home(request):
    # Создаем тестовый сервер, если его нет
    if not Server.objects.exists():
        Server.objects.create(
            name="MadiMinecraft Main",
            ip_address="mc.madiminecraft.com",
            port=25565,
            is_online=False
        )
    
    servers = Server.objects.all()
    return render(request, 'servers/home.html', {'servers': servers})