from django.contrib import admin
from .models import SaleInvoice, SaleInvoiceLine

admin.site.register(SaleInvoice)
admin.site.register(SaleInvoiceLine)
