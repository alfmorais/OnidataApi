from payments.models import Payment
from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "loan",
            "installment_amount",
            "installment_number",
            "date",
            "is_paid",
        ]


class PaymentUpdateSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    is_paid = serializers.BooleanField(required=True)


class BalanceSerializer(serializers.Serializer):
    loan_id = serializers.UUIDField()
    installments_paid = serializers.IntegerField()
    installments_missing_payment = serializers.IntegerField()
    total_installments = serializers.IntegerField()
    amount_paid = serializers.CharField()
    amount_missing_payment = serializers.CharField()
