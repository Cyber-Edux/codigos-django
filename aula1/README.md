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


