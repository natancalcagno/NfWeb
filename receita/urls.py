from django.urls import path, include
from receita.views import home, contato, sobre

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]