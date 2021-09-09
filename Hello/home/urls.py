from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.first, name='home'),
    path("choice", views.choice, name='choice'),
    path("send", views.send, name='send'),
    path("about", views.about, name= 'about'),
    path("gf", views.gf, name='gf')
]
