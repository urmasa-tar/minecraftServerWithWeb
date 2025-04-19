from django.shortcuts import render
from .models import Server

def home(request):
    servers = Server.objects.all()
    return render(request, 'servers/home.html', {'servers': servers})