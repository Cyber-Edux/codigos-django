from django.shortcuts import render
from .models import Pessoa


def index_page(request):
    return render(request, 'index.html', {
        'pessoas': Pessoa.objects.all()
    })
