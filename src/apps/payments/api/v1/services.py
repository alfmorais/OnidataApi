from .repositories import (
    BalancePaymentRepository,
    CreatePaymentRepository,
    ListAllPaymentsRepository,
    UpdatePaymentRepository,
)


class PaymentListService:
    def __init__(self, repository=ListAllPaymentsRepository()):
        self.repository = repository

    def handle(self, loan_uuid, is_paid=True):
        return self.repository.handle(loan_uuid, is_paid)


class PaymentUpdateService:
    def __init__(self, repository=UpdatePaymentRepository()):
        self.repository = repository

    def handle(self, loan_uuid, payload):
        return self.repository.handle(loan_uuid, payload)


class BalanceService:
    def __init__(self, repository=BalancePaymentRepository()):
        self.repository = repository

    def handle(self, loan_uuid):
        return self.repository.handle(loan_uuid)


class CreatePaymentsService:
    def __init__(self, repository=CreatePaymentRepository()):
        self.repository = repository

    def handle(self, cet_amount, installments, loan):
        installments_amount = cet_amount / installments
        return self.repository.handle(installments_amount, installments, loan)
