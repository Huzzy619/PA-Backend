from rest_framework import serializers


class WalletSerializer(serializers.Serializer):
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)


