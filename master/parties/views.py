from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Parties
from .serializers import PartiesSerializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt




def parties_list(request):
    if request.method=='GET':
        parties = Parties.objects.all()
        serializer = PartiesSerializers(parties, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method=='POST':
        parties = JSONParser().parse(request)
        serializer = PartiesSerializers(data=parties)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



def customers_list(request):
    customers = Parties.objects.filter(is_customer=True)
    serializer = PartiesSerializers(customers, many=True)
    return JsonResponse(serializer.data, safe=False)

def vendors_list(request):
    vendors = Parties.objects.filter(is_vendor=True)
    serializer = PartiesSerializers(vendors, many=True)
    return JsonResponse(serializer.data, safe=False)
