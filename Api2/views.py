from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework import viewsets
from configuration.models import Contact,About
#from django_filters.rest_framework import DjangoFilterBackend

# import json
# from django.http import JsonResponse


class contact(viewsets.ModelViewSet):
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()
    
class about(viewsets.ModelViewSet):
    serializer_class = AboutSerializers
    queryset = About.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['categorie',]