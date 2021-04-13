from django.urls import path

from . import views

app_name = 'caesar'
urlpatterns = [
    path('caesar-cipher', views.index, name='index'),
    path('caesar-cipher-ajax', views.decipher, name='decipher'),
]
