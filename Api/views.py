from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework import viewsets
from blog.models import Categorie, Article, Tag, Commentaire
from configuration.models import Contact,About
#from django_filters.rest_framework import DjangoFilterBackend

# import json
# from django.http import JsonResponse


class categorie_list(viewsets.ModelViewSet):
    serializer_class = CategorieSerializers
    queryset = Categorie.objects.all()
    
class article(viewsets.ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['categories', ]
    
   
class categorie_detail(viewsets.ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['nom', ]
  
  
class tag(viewsets.ModelViewSet):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['nom', ]


class commentaire(viewsets.ModelViewSet):
    serializer_class = CommentaireSerializers
    queryset = Commentaire.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['nom', ]



    
    