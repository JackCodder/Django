from django.http import HttpResponse
from django.shortcuts import render

def index(request): #HttpRequest
    return HttpResponse('Страница приложения women')


def categories(reques):
    return HttpResponse('<h1>Статьи по категориям</h1>')