from .repositories import (
    BalancePaymentRepository,
    CreatePaymentRepository,
    ListAllPaymentsRepository,
    UpdatePaymentRepository,
)


class PaymentListService:
    def __init__(self, repository=ListAllPaymentsRepository()):
        self.repository = repository

    def handle(self, loan_uuid):
        return self.repository.handle(loan_uuid)


class PaymentUpdateService:
    def __init__(self, repository=UpdatePaymentRepository()):
        self.repository = repository

    def handle(self, payload):
        return self.repository.handle(payload)


class BalanceService:
    def __init__(self, repository=BalancePaymentRepository()):
        self.repository = repository

    def total_amount(self, queryset):
        amount_list = [payment.installment_amount for payment in queryset]
        return sum(amount_list)

    def handle(self, loan_uuid):
        queryset = self.repository.handle(loan_uuid)
        installments_paid = []
        installments_missing_payment = []

        for payment in queryset:

            if payment.is_paid:
                installments_paid.append(payment)
            else:
                installments_missing_payment.append(payment)

        pending_payment = self.total_amount(installments_missing_payment)

        response = {
            "loan_id": loan_uuid,
            "installments_paid": len(installments_paid),
            "installments_missing_payment": len(installments_missing_payment),
            "total_installments": len(installments_paid)
            + len(installments_missing_payment),
            "amount_paid": self.total_amount(installments_paid),
            "amount_missing_payment": pending_payment,
        }
        return response


class CreatePaymentsService:
    def __init__(self, repository=CreatePaymentRepository()):
        self.repository = repository

    def handle(self, cet_amount, installments, loan):
        installments_amount = float(cet_amount) / installments
        return self.repository.handle(installments_amount, installments, loan)
