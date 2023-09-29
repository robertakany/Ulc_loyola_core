from django.contrib import admin
from django.urls import path
from main import views

urlpatterns=[
path('', views.home, name='home'),
path('page/', views.home1, name='home1'),


]