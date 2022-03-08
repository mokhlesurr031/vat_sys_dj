from django.urls import path 
from . import views

urlpatterns = [
    path('list/', views.parties_list, name='parties_list'),
    path('list/customers/', views.customers_list, name='customers_list'),
    path('list/vendors/', views.vendors_list, name='vendors_list'),
]