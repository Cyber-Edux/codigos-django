# Aula 1

O objetivo desta aula é criar um "Hello World" em Django. Este Hello World é um sistema web mínimo em Django, que recebe requisições GET e retorna pacotes HTTP com frases como "Hello World" e "Welcome", que aparecem no navegador.

## Passo-a-passo

1. Crie um projeto Django pelo terminal com o seguinte comando:
```sh
django-admin startproject aula1
```

2. No diretório aula1, deixe o arquivo urls.py da seguinte forma:

```python
from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello World!')

def welcome(request):
    return HttpResponse('Welcome!')

def hello_name(request, name):
    return HttpResponse(f'Hello, {name.upper()}!')

urlpatterns = [
    path('', hello_world),
    path('welcome/', welcome),
    path('hello/<str:name>/', hello_name)
]
```

Este código cria 3 views: ``hello_world``, ``welcome`` e ``hello_name``. Cada view é uma função que define a forma como o sistema deve reagir às requisições feitas pelo navegador através de uma URL. Neste código, as URLs associadas às 3 views são, respectivamente, ``/`` (apenas o domínio ou o endereço do localhost), ``welcome/`` e ``hello/<str:name>`` (onde ``<str:name>`` deve ser substituído por um nome qualquer).     

1. Para testar o projeto, crie um servidor local com o seguinte comando no terminal:
```
python manage.py runserver
```

## Modo de uso

Considere que o endereço usado pelo servidor de teste é ``http://127.0.0.1:8000/``.

1. Ao acessar ``http://127.0.0.1:8000/`` pelo navegador, a frase "Hello World!" deve ser recebida.
2. Ao acessar ``http://127.0.0.1:8000/welcome/``, a frase "Welcome!" deve ser recebida.
3. Ao acessar ``http://127.0.0.1:8000/hello/fulano``, a frase "Welcome, FULANO!" deve ser recebida.
