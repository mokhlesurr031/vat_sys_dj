from django.contrib import admin
from .models import ProductVariant, Product, HSCode


admin.site.register(HSCode)
admin.site.register(Product)
admin.site.register(ProductVariant)
