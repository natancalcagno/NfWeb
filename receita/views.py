from django.shortcuts import render
from util.recipes.factory import make_recipe

def home(request):
    return render(request, 'receita/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })

def recipe(request, id):
    return render(request, 'receita/pages/recipe-view.html', context= {
        'recipe': make_recipe(),
    })