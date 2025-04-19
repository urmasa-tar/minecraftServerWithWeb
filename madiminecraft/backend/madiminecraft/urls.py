from django.contrib import admin
from django.urls import path
from servers import views as servers_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', servers_views.home, name='home'),
]