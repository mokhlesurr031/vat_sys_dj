from django.shortcuts import render
from purchase.models import PurchaseInvoice, PurchaseInvoiceLine
from django.http import HttpResponse, JsonResponse
from sales.models import SaleInvoice, SaleInvoiceLine


# Create your views here.

def calculate_vat():
    pass

def vat_on_so(request):
    so_data_list = []
    so_data = {}
    so = SaleInvoice.objects.all()
    for s in so:
        print("SSSS", s)
        so_data['so_id'] = "SO-"+str(s.id)
        so_data['customer'] = s.customer.name
        so_data['date'] = str(s.order_deadline)
        so_line = SaleInvoiceLine.objects.filter(si_id = s.id)
        vat_total = 0
        so_total = 0
        for sl in so_line:
            so_total += sl.total
            vat_total += sl.total*(sl.vat/100)
        so_data['so_total'] = so_total
        so_data['vat_total'] = vat_total
        so_data_list.append(so_data)
        vat_total = 0
        so_total = 0
        so_data = {}

    print("SO DATA", so_data)

    print(so_data_list)
    
    return JsonResponse({'result': so_data_list}) 

def vat_on_po(request):
    po_data_list = []
    po_data = {}
    po = PurchaseInvoice.objects.all()
    for p in po:
        po_data['po_id'] = "PO-"+str(p.id)
        po_data['vendor'] = p.vendor.name
        po_data['date'] = str(p.order_deadline)
        po_line = PurchaseInvoiceLine.objects.filter(pi_id = p.id)
        vat_total = 0
        po_total = 0
        for pl in po_line:
            po_total += pl.total
            vat_total += pl.total*(pl.vat/100)
        po_data['po_total'] = po_total
        po_data['vat_total'] = vat_total
        po_data_list.append(po_data)
        vat_total = 0
        po_total = 0
        po_data = {}
    
    return JsonResponse({'result': po_data_list})