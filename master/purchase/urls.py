from django.urls import path
from . import views

urlpatterns = [
    path('', views.purchase_list, name='purchase_list'),
    path('details/<int:id>/', views.purchase_details, name='purchase_details'),
    path('product_details/<int:id>/', views.product_details_for_purchase, name='product_details_for_purchase'),
]