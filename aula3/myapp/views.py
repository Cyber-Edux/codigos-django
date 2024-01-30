from django.shortcuts import render
from datetime import datetime
from random import randint

def home(request):
    dados = {
        'nomes': ['Fulano', 'Ciclano', 'Beltrano'],
        'horario': datetime.now().strftime('%H:%M:%S'),
        'numero': randint(0, 100)
    }
    return render(request, 'index.html', dados)