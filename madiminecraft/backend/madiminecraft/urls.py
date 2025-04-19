from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('servers.urls')),
    path('accounts/', include('accounts.urls')),
    path('ratings/', include('ratings.urls')),
]