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
    def handle(self, loan_uuid, is_paid):
        payments = self.model.objects.filter(loan=loan_uuid, is_paid=is_paid)
        return payments


class UpdatePaymentRepository(PaymentBaseRepository):
    def handle(self, loan_uuid, payload):
        payment = self.model.objects.filter(
            loan=loan_uuid,
            id=payload["id"],
        ).first()

        if payment.count() == 0:
            raise ValidationError(
                detail={"error": "Payment not found"},
                code=HTTP_404_NOT_FOUND,
            )

        payment.is_paid = payload["is_paid"]
        payment.date = now()
        payment.save()
        return payment


class BalancePaymentRepository(PaymentBaseRepository):
    def handle(self, loan_uuid): ...


class CreatePaymentRepository(PaymentBaseRepository):
    def handle(self, installments_amount, installments, loan):
        bulk_create_payment_list = []
        final_iterator = installments + 1
        formated_installments_amount = str(round(installments_amount, 2))

        for installment_number in range(1, final_iterator, 1):
            payment = self.model(
                loan=loan,
                installment_amount=formated_installments_amount,
                installments_number=installment_number,
                is_paid=False,
            )
            bulk_create_payment_list.append(payment)

        try:
            self.model.objects.bulk_create(bulk_create_payment_list)

        except (IntegrityError, OperationalError) as error:
            raise ValidationError(
                detail={"error": error},
                code=HTTP_500_INTERNAL_SERVER_ERROR,
            )
