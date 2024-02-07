from uuid import uuid4

import pytest
from src.apps.payments.api.v1.services import (
    BalanceService,
    CreatePaymentsService,
    PaymentListService,
    PaymentUpdateService,
)

pytestmark = pytest.mark.django_db


def test_payment_list_service_success(loan, payment_with_loan):
    loan.id = uuid4()
    loan.save()

    payment_with_loan.loan = loan
    payment_with_loan.save()

    service = PaymentListService()
    response = service.handle(loan_uuid=loan.id)

    assert response[0].id == payment_with_loan.id


def test_payment_update_service_success(loan, payment_with_loan):
    loan.id = uuid4()
    loan.save()

    payment_with_loan.id = uuid4()
    payment_with_loan.loan = loan
    payment_with_loan.save()

    service = PaymentUpdateService()
    response = service.handle(
        payload={
            "id": payment_with_loan.id,
            "is_paid": True,
        }
    )

    assert response.is_paid is True


def test_balance_service_success(loan, payment_with_loan):
    loan.id = uuid4()
    loan.save()

    payment_with_loan.id = uuid4()
    payment_with_loan.loan = loan
    payment_with_loan.save()

    service = BalanceService()
    response = service.handle(loan_uuid=loan.id)

    assert sorted(response.keys()) == sorted(
        [
            "loan_id",
            "installments_paid",
            "installments_missing_payment",
            "total_installments",
            "amount_paid",
            "amount_missing_payment",
        ]
    )
    assert isinstance(response, dict)


def test_create_payment_success(loan):
    service = CreatePaymentsService()
    response = service.handle(
        cet_amount="10000",
        installments=5,
        loan=loan,
    )

    assert response is None
