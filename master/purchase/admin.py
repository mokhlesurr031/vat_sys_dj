from django.contrib import admin
from .models import PurchaseInvoice, PurchaseInvoiceLine

admin.site.register(PurchaseInvoice)
admin.site.register(PurchaseInvoiceLine)
