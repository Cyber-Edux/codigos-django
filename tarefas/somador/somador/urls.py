
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def soma(request, a, b):
    return HttpResponse(f'{a+b}')


urlpatterns = [
    path('soma/<int:a>/<int:b>', soma)
]
