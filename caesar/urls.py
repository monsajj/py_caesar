from django.urls import path

from . import views

urlpatterns = [
    path('caesar-cipher', views.index, name='index'),
]