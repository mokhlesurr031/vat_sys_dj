from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('products.urls')),
    path('parties/', include('parties.urls')),
    path('', include('index.urls')),
    path('purchase/', include('purchase.urls')),
    path('sales/', include('sales.urls')),
]
