from rest_framework import serializers
from .models import PurchaseInvoice, PurchaseInvoiceLine


class PurchaseInvoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoice
        fields = '__all__'


class PurchaseInvoiceLineSerializers(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoiceLine
        fields = '__all__'

