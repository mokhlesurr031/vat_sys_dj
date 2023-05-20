from django.db import models
from parties.models import Parties
from products.models import Product, ProductVariant

uom = [
    ('number', 'NMB'),
    ('kg', 'KGM')
]

product_type = [
    ('raw_material', 'Raw Material'),
    ('finished_good', 'Finished Good'),
]

class SaleInvoice(models.Model):
    customer = models.ForeignKey(Parties, on_delete=models.CASCADE)
    address = models.CharField(max_length=455, null=True)
    order_deadline = models.DateField(auto_now_add=True, null=True)
    mobile = models.CharField(max_length=25, null=True)
    email = models.CharField(max_length=200, null=True)
    invoice_amount = models.FloatField(default=0, null=True)

    # def __str__(self):
    #     return self.vendor

class SaleInvoiceLine(models.Model):
    si_id = models.ForeignKey(SaleInvoice, on_delete=models.CASCADE, null=True)
    hs_code = models.CharField(max_length=200, null=True)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    product_type = models.CharField(choices=product_type, max_length=200)
    uom = models.CharField(choices=uom, max_length=25)
    cd = models.FloatField(default=0)
    sd = models.FloatField(default=0)
    vat = models.FloatField(default=0)
    ait = models.FloatField(default=0)
    rd = models.FloatField(default=0)
    atv = models.FloatField(default=0)
    tti = models.FloatField(default=0)
    tti_amount = models.FloatField(default=0)
    total = models.FloatField(default=0)
    total_payable = models.FloatField(default=0)
    remark = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.hs_code







