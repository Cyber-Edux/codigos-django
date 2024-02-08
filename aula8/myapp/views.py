from django.shortcuts import render
from .models import Pessoa
from django.http import HttpResponseRedirect, HttpResponseBadRequest

def cadastro_page(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        pais = request.POST.get('pais')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        pessoa = Pessoa()
        pessoa.nome = nome
        pessoa.pais = pais
        pessoa.estado = estado
        pessoa.cidade = cidade
        pessoa.save()
        return HttpResponseRedirect('/consulta')
    else:
        return HttpResponseBadRequest()

def consulta_page(request):
    return render(request, 'consulta.html')