# Aula 2

**Objetivo:** criar um site em Django com apenas uma página HTML com a frase "Hello World".

## Passo-a-passo

1. Crie um projeto Django com o comando ``django-admin startproject <nome>``. Nesta aula, no lugar de ``<nome>``, é utilizado o nome ``aula2``.
2. Para implementar um *site* em Django, é necessário criar um *app* dentro do projeto com o comando ``python manage.py startapp <nome>`` (o nome utilizado nesta aula é ``myapp``). Este *app* conterá as *views* e *models* do *site*.
3. Crie um diretório ``myapp/templates``.
4. Crie um arquivo ``index.html`` no diretório ``myapp/templates`` e preencha este arquivo com um *Hello World* simples em HTML.
5. No arquivo ``myapp/views.py``, coloque a seguinte função:
```py
def index(request):
    return render(request, 'index.html')
```
Esta função é a *view* que renderiza a página *index.html*.
6. Modifique o arquivo ``aula2/urls.py`` para que a URL raiz do site seja associada à view ``index``. O conteúdo deste arquivo deve ficar da seguinte forma:

```py
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
]
```
7. Teste o site com o comando ``python manage.py runserver``.