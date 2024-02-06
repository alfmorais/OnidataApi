from payments.models import Payment
from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "loan",
            "installment_amount",
            "date",
            "is_paid",
        ]


class PaymentUpdateSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    is_paid = serializers.BooleanField(required=True)


class BalanceSerializer(serializers.Serializer):
    ...
