from django.shortcuts import render
from .models import HSCode, ProductVariant, Product
from django.http import HttpResponse, JsonResponse
from .serializers import HSCodeSerializers, ProductSerializers, ProductVariantSerializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


def hs_code_list(request):
    if request.method=='GET':
        hs_code = HSCode.objects.all()
        serializer = HSCodeSerializers(hs_code, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method=='POST':
        pass



def product_variant_list(request):
    if request.method=='GET':
        product_variant = ProductVariant.objects.all()
        serializer = ProductVariantSerializers(product_variant, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method=='POST':
        pass


def product_list(request):
    if request.method=='GET':
        product = Product.objects.all()
        serializer = ProductSerializers(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method=='POST':
        pass
