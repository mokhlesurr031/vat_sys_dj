from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import PurchaseInvoice, PurchaseInvoiceLine
from .serializers import PurchaseInvoiceSerializers, PurchaseInvoiceLineSerializers
from django.views.decorators.csrf import csrf_exempt
import pdb
import json 



@csrf_exempt
def purchase_list(request):
    if request.method == 'GET':
        final_output = []
        inv_data = {}
        purchase_inv = PurchaseInvoice.objects.all()
        for pi in purchase_inv:
            vendor_data = {
                'vendor': pi.vendor.name,
                'email': pi.email,
                'address': pi.address,
                'order_deadline': str(pi.order_deadline),
                'mobile': pi.mobile,
            }
            inv_line = PurchaseInvoiceLine.objects.filter(pi_id = pi.id)
            inl = {}
            for il in inv_line:
                inv_line_data = {
                    'hs_code': il.hs_code,
                    'product_variant': il.product_variant.name,
                    'product_id': il.product_id.name,
                    'product_type': il.product_type,
                    'uom': il.uom,
                    'cd': il.cd,
                    'sd': il.sd,
                    'vat': il.vat,
                    'ait': il.ait,
                    'rd': il.rd,
                    'atv': il.atv,
                    'total': il.total,
                    'remark': il.remark,
                }
                inl[il.product_id.name] = inv_line_data
            inv_data['vendor'] = [vendor_data]
            inv_data['products'] = [inl]
            final_output.append(inv_data)
        return HttpResponse(json.dumps({'result': final_output}))


    if request.method=='POST':
        purchase = JSONParser().parse(request)
        print(purchase)
        serializer = PurchaseInvoiceSerializers(data=purchase)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)