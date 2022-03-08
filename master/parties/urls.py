from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='parties_index'),
]