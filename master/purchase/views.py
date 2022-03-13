from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import PurchaseInvoice, PurchaseInvoiceLine
from .serializers import PurchaseInvoiceSerializers, PurchaseInvoiceLineSerializers
from django.views.decorators.csrf import csrf_exempt
import pdb
import json
from products.models import Product



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
            inv_data = {}
        print(final_output)
        return HttpResponse(json.dumps({'result': final_output}))


    if request.method=='POST':
        purchase = JSONParser().parse(request)
        print(purchase)
        vendor = purchase['result'][0]['vendor']
        products = purchase['result'][0]['products']

        vendor_mobile = vendor['mobile']
        vendor_email = vendor['email']
        vendor_address = vendor['address']
        vendor_order_deadline = vendor['order_deadline']
        vendor_name = vendor['vendor']


        products_id = products['product_id']
        products_name = products['product_name']
        products_hs_code_id = products['hs_code_id']
        products_hs_code = products['hs_code']
        products_variant_id = products['product_variant_id']
        products_variant = products['product_variant']
        products_type = products['product_type']
        products_uom = products['uom']
        products_cd = products['cd']
        products_sd = products['sd']
        products_vat = products['vat']
        products_ait = products['ait']
        products_rd = products['rd']
        products_atv = products['atv']
        print('---------------------------------')

        vendor_data = json.dumps({'vendor': vendor_name, 'email': vendor_email, 'address': vendor_address, 'order_deadline': vendor_order_deadline, 'mobile': vendor_mobile})
        print(vendor_data)

        # pi_id
        # hs_code
        # product_variant
        # product_id
        # product_type
        # uom
        # cd
        # sd
        # vat
        # ait
        # rd
        # atv
        # total
        # remark

        products_data = json.dumps({'hs_code': products_hs_code, 'product_variant': products_variant, 'product_id': products_id, 'product_type': products_type, 'uom': products_uom, 'cd':products_cd, 'sd': products_sd,
                                    'vat': products_vat, 'ait': products_ait, 'rd': products_rd, 'atv': products_atv})

        print('---------------------------------')
        print(products_data)

        print('---------------------------------')




        return HttpResponse(json.dumps({'success': 1}))


@csrf_exempt
def product_details_for_purchase(request, id):
    if request.method=='POST':
        prod_id = id
        product_data = Product.objects.get(id=prod_id)

        product_dict = {
            'product_id': product_data.id,
            'product_name': product_data.name,
            'hs_code_id': product_data.product_category.hs_code.id,
            'hs_code': product_data.product_category.hs_code.hs_code,
            'product_variant_id': product_data.product_category.id,
            'product_variant': product_data.product_category.name,
            'product_type': product_data.product_type,
            'uom': product_data.product_category.hs_code.uom,
            'cd': product_data.product_category.hs_code.cd,
            'sd': product_data.product_category.hs_code.sd,
            'vat': product_data.product_category.hs_code.vat,
            'ait': product_data.product_category.hs_code.ait,
            'rd': product_data.product_category.hs_code.rd,
            'atv': product_data.product_category.hs_code.atv,
        }

        json_prod_dict = json.dumps(product_dict)


        return HttpResponse(json_prod_dict)
