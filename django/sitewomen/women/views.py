from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

def index(request): #HttpRequest
    return HttpResponse('Страница приложения women')


def categories(reques, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id:{cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug:{cat_slug}</p>')


def archive(request, year):
    if year > 2024:
        return redirect('cats', 'moves')
    return HttpResponse((f"<h1>Архив по годам</h1><p >{year}</p>"))

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
