from django.shortcuts import render
from .models import Article, Commentaire, Tag, Categorie


def index(request):
    articles = Article.objects.all()
    data = {
        'articles':articles,
    }
    return render(request, 'pages1/index.html', data)


def fashion(request):
    data = {

    }
    return render(request, 'pages1/fashion.html', data)



def travel(request):
    data = {

    }
    return render(request, 'pages1/travel.html', data)


def single(request):
    data = {

    }
    return render(request, 'pages1/single.html', data)
