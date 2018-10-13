from rest_framework import serializers
from .models import Inmate

class InmateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmate
        fields = '__all__'


