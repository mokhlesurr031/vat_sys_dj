from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import PurchaseInvoice, PurchaseInvoiceLine
from .serializers import PurchaseInvoiceSerializers, PurchaseInvoiceLineSerializers
from django.views.decorators.csrf import csrf_exempt




def purchase_list(request):
    if request.method == 'GET':
        purchase_inv = PurchaseInvoice.objects.all()
        serializer = PurchaseInvoiceSerializers(purchase_inv, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method=='POST':
        purchase = JSONParser().parse(request)
        print(purchase)
        serializer = PurchaseInvoiceSerializers(data=purchase)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)