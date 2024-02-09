from django.shortcuts import render
from .models import Pessoa
from django.http import HttpResponseRedirect, HttpResponseBadRequest

def index(request):
    return HttpResponseRedirect('/consulta')

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
    #pessoas = Pessoa.objects.all()
    #pessoas = Pessoa.objects.filter(estado='Mato Grosso')
    pessoas = Pessoa.objects.raw('select * from myapp_pessoa where estado="Mato Grosso"')
    #SELECT * FROM myapp_pessoa WHERE estado="Mato Grosso"
    return render(request, 'consulta.html', {
        'pessoas': pessoas
    })