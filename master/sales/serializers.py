from rest_framework import serializers
from .models import SaleInvoice, SaleInvoiceLine


class SaleInvoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = SaleInvoice
        fields = '__all__'


class SaleInvoiceLineSerializers(serializers.ModelSerializer):
    class Meta:
        model = SaleInvoiceLine
        fields = '__all__'

