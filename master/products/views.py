from django.shortcuts import render
from .models import HSCode, ProductVariant, Product
from django.http import HttpResponse

def index(request, pk):
    product = Product.objects.get(id=pk)
    print(product)
    sd = product.product_category.hs_code.sd
    return HttpResponse(sd)

