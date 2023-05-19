from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import SaleInvoice, SaleInvoiceLine
from .serializers import SaleInvoiceSerializers, SaleInvoiceLineSerializers
from django.views.decorators.csrf import csrf_exempt
import pdb
import json
from products.models import Product
from parties.models import Parties



@csrf_exempt
def sales_list(request):
    if request.method == 'GET':
        final_output = []
        inv_data = {}
        sales_inv = SaleInvoice.objects.all()
        for si in sales_inv:
            customer_data = {
                'id': si.id,
                'customer': si.customer.name,
                'email': si.email,
                'address': si.address,
                'order_deadline': str(si.order_deadline),
                'mobile': si.mobile,
                'invoice_amount': si.invoice_amount,
            }

            inv_line = SaleInvoiceLine.objects.filter(si_id = si.id)
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
                    'tti': il.tti,
                    'tti_amount': il.tti_amount,
                    'total': il.total,
                    'remark': il.remark,
                }
                inl[il.product_id.name] = inv_line_data
            inv_data['customer'] = [customer_data]
            inv_data['products'] = [inl]

            final_output.append(inv_data)
            inv_data = {}
        # print(final_output)
        return HttpResponse(json.dumps({'result': final_output}))




    if request.method=='POST':
        sales = eval(request.body)
        customer = sales['result'][0]['customer']
        products = sales['result'][0]['products']

        print("Customer: ", customer)
        print("PRODUCTS: ", products)

        customer_mobile = customer['mobile']
        customer_email = customer['email']
        customer_address = customer['address']
        customer_order_deadline = customer['order_deadline']
        customer_name = customer['customer']
        # vendor_data = json.dumps({'vendor': vendor_name, 'email': vendor_email, 'address': vendor_address,
        #                           'order_deadline': vendor_order_deadline, 'mobile': vendor_mobile})

        customer_id = Parties.objects.get(email=customer_email).id


        si = SaleInvoice.objects.create(
            mobile = customer_mobile,
            email = customer_email,
            address= customer_address,
            order_deadline= customer_order_deadline,
            customer_id = customer_id,
        )
        si_id = si.id
        print("SI ID", type(si_id))


        for prod in products:
            print("===========")
            print(prod)
            print("++++++++++++")
            SaleInvoiceLine.objects.create(
                si_id_id = si_id,
                hs_code=prod['hs_code'],
                product_variant_id=prod['product_variant_id'],
                product_id_id = prod['product_id'],
                product_type = prod['product_type'],
                uom = prod['uom'],
                cd = prod['cd'],
                sd = prod['sd'],
                vat = prod['vat'],
                ait = prod['ait'],
                rd = prod['rd'],
                atv = prod['atv'],
                # tti = prod['tti'],
                tti_amount = 0,
                total = 0,
                remark= 'Holy Shit',

            )

        return HttpResponse(json.dumps({'success': 1}))


@csrf_exempt
def product_details_for_sales(request, id):
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
            'tti': product_data.product_category.hs_code.tti,
        }

        json_prod_dict = json.dumps(product_dict)

        return HttpResponse(json_prod_dict)


from django.core import serializers

@csrf_exempt
def sales_details(request, id):
    if request.method == 'GET':
        inv_id = id
        try:
            sales_data = SaleInvoice.objects.get(id=inv_id)
            sales_data_details = SaleInvoiceLine.objects.filter(si_id=inv_id)
            
            # Convert the Parties object to a JSON-serializable format
            parties_data = serializers.serialize('json', [sales_data.customer])


            # Construct the nested dictionary
            data = {
                'sales_data': {
                    'id': sales_data.id,
                    'invoice_total': 0,
                    'address': sales_data.address,
                    'mobile': sales_data.mobile,
                    'email': sales_data.email,
                    'order_deadline': str(sales_data.order_deadline),
                    'customer': sales_data.customer.name,
                    # Add more fields as needed
                },
                'sales_data_details': [
                    {
                        'id': detail.id,
                        'hs_code': detail.hs_code,
                        'product_variant': detail.product_variant.name,
                        'product_id': detail.product_id.name if detail.product_id else None,
                        'product_type': detail.product_type,
                        'uom': detail.uom,
                        'cd': detail.cd,
                        'sd': detail.sd,
                        'vat': detail.vat,
                        'ait': detail.ait,
                        'rd': detail.rd,
                        'atv': detail.atv,
                        'total': detail.total,
                        'remark': detail.remark,
                    }
                    for detail in sales_data_details
                ]
            }

            invoice_total = 0
            for i in data['sales_data_details']:
                invoice_total+=i['total']
            data['sales_data']['invoice_total'] = invoice_total
            print(invoice_total)
            print("+++++++++++++++++++++++++")
            return JsonResponse(data)

        except SaleInvoice.DoesNotExist:
            data = {'error': 'Sales invoice not found'}
            return HttpResponse(json.dumps(data), status=404)

        except Exception as e:
            data = {'error': str(e)}
            return HttpResponse(json.dumps(data), status=500)