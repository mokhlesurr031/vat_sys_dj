from django.db import models

# Create your models here.


product_type = [
    ('raw_material', 'Raw Material'),
    ('finished_good', 'Finished Good'),
]

uom = [
    ('number', 'NMB'),
    ('kg', 'KGM')
]

class HSCode(models.Model):
    hs_code = models.CharField(max_length=155)
    description = models.CharField(max_length=455)
    uom = models.CharField(choices=uom, max_length=25)
    cd = models.FloatField(default=0)
    sd = models.FloatField(default=0)
    vat = models.FloatField(default=0)
    ait = models.FloatField(default=0)
    rd = models.FloatField(default=0)
    atv = models.FloatField(default=0)

    def __str__(self):
        return self.hs_code


class ProductVariant(models.Model):
    name = models.CharField(max_length=200)
    hs_code = models.ForeignKey(HSCode, on_delete = models.CASCADE) 
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    product_category = models.ForeignKey(ProductVariant, on_delete = models.CASCADE) 
    manufacturer = models.CharField(max_length=200)
    product_type = models.CharField(choices=product_type, max_length=200)

    # purchase_price = models.FloatField()
    # sale_price = models.FloatField()
    available_in_po = models.BooleanField(default=0)
    available_in_so = models.BooleanField(default=0)
    description = models.TextField()


    # hs_code = models.ForeignKey(HSCode)


    def __str__(self):
        return self.name