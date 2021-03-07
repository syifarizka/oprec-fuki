from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('savematkul/', views.savematkul, name='savematkul'),
    path('savetugas/<int:pk>', views.savetugas, name='savetugas'),
]
