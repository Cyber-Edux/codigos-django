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
