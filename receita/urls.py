from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="receita-home"),
    path('receita/<int:id>/', views.recipe, name="receitas-receita"),
    
]