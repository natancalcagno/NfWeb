from django.shortcuts import render

def home(request):
    return render(request, 'receita/home.html')

def contato(request):
    return render(request, 'receita/contato.html')

def sobre(request):
    return render(request, 'receita/sobre.html')