from django.urls import path, include
from receita.views import home

urlpatterns = [
    path('', home, name='home'),
    
]