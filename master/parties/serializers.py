from rest_framework import serializers
from .models import Parties


class PartiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parties
        fields = '__all__'