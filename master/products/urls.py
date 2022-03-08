from django.urls import path 
from . import views


urlpatterns = [
    path('hs_code/', views.hs_code_list, name='hs_code_list'),
    path('product_variant/', views.product_variant_list, name='product_variant_list'),
    path('product_list/', views.product_list, name='product_list'),
]