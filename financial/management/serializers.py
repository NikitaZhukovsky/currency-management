from rest_framework import serializers
from management.models import Currency, ExchangesRate, Subscription


class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('name', 'code')

