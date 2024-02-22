"""
TODO: A estrutura inteira de repositórios é desnecessária e os recursos do próprio REST
framework não foram aproveitados (ListCreateView, ModelSerializers, etc)
"""

from django.db.utils import IntegrityError, OperationalError
from django.utils.timezone import now
from payments.models import Payment
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from rest_framework.validators import ValidationError


class PaymentBaseRepository:
    def __init__(self, model=Payment):
        self.model = model


class ListAllPaymentsRepository(PaymentBaseRepository):
    def handle(self, loan_uuid):
        payments = self.model.objects.filter(loan=loan_uuid)

        if payments.count() == 0:
            raise ValidationError(
                detail={"error": "Payments not found"},
                code=HTTP_404_NOT_FOUND,
            )

        return payments


class UpdatePaymentRepository(PaymentBaseRepository):
    def handle(self, payload):
        queryset = self.model.objects.filter(
            id=payload["id"],
        )

        if queryset.count() == 0:
            raise ValidationError(
                detail={"error": "Payment not found"},
                code=HTTP_404_NOT_FOUND,
            )

        payment = queryset.first()
        payment.is_paid = payload["is_paid"]
        payment.date = now()
        payment.save()
        return payment


class BalancePaymentRepository(PaymentBaseRepository):
    def handle(self, loan_uuid):
        queryset = self.model.objects.filter(
            loan__id=str(loan_uuid),
        )

        if queryset.count() == 0:
            raise ValidationError(
                detail={"error": "Payments not found"},
                code=HTTP_404_NOT_FOUND,
            )

        return queryset


class CreatePaymentRepository(PaymentBaseRepository):
    def handle(self, installments_amount, installments, loan):
        bulk_create_payment_list = []
        final_iterator = installments + 1
        formated_installments_amount = str(round(installments_amount, 2))

        for installment_number in range(1, final_iterator, 1):
            payment = self.model(
                loan=loan,
                installment_amount=formated_installments_amount,
                installment_number=installment_number,
                is_paid=False,
                date=None,
            )
            bulk_create_payment_list.append(payment)

        try:
            self.model.objects.bulk_create(bulk_create_payment_list)

        except (IntegrityError, OperationalError) as error:
            raise ValidationError(
                detail={"error": error},
                code=HTTP_500_INTERNAL_SERVER_ERROR,
            )
