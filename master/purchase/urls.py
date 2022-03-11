from django.urls import path
from . import views

urlpatterns = [
    path('', views.purchase_list, name='purchase_list'),
    path('product_details/<int:id>/', views.product_details_for_purchase, name='product_details_for_purchase'),
]