from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('fashion/', views.fashion, name="fashion"),
    path('travel/', views.travel, name="travel"),
    path('single/', views.single, name="single"),
]