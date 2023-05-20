from django.urls import path
from . import views

urlpatterns = [
    path('po/', views.vat_on_po, name='vat_on_po'),
    path('so/', views.vat_on_so, name='vat_on_so')
]