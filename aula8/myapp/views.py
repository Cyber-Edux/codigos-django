from django.shortcuts import render


def cadastro_page(request):
    return render(request, 'cadastro.html')


def consulta_page(request):
    return render(request, 'consulta.html')