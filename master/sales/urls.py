from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_list, name='sales_list'),
    path('details/<int:id>/', views.sales_details, name='sales_details'),

    path('sales_details/<int:id>/', views.product_details_for_sales, name='product_details_for_sales'),
]