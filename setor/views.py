from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def listar_produtos_view(request):