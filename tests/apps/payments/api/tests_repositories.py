from unittest.mock import patch
from uuid import uuid4

import pytest
from django.db.utils import IntegrityError, OperationalError
from rest_framework.validators import ValidationError
from src.apps.payments.api.v1.repositories import (
    BalancePaymentRepository,
    CreatePaymentRepository,
    ListAllPaymentsRepository,
    PaymentBaseRepository,
    UpdatePaymentRepository,
)

pytestmark = pytest.mark.django_db


def test_payment_base_repository(payment_with_loan):
    repository = PaymentBaseRepository()

    assert isinstance(payment_with_loan, repository.model)


def test_list_all_payments_repository_error():
    repository = ListAllPaymentsRepository()
    loan_uuid = uuid4()

    with pytest.raises(ValidationError) as error:
        repository.handle(loan_uuid=loan_uuid)

    assert error.type == ValidationError
    assert error.value.status_code == 400


def test_list_all_payments_repository_success(loan, payment_with_loan):
    loan.id = uuid4()
    loan.save()

    payment_with_loan.loan = loan
    payment_with_loan.id = uuid4()
    payment_with_loan.save()

    repository = ListAllPaymentsRepository()
    response = repository.handle(loan_uuid=loan.id)

    assert response[0].id == payment_with_loan.id


def test_update_payment_repository_error():
    repository = UpdatePaymentRepository()
    payload = {"id": uuid4(), "is_paid": True}

    with pytest.raises(ValidationError) as error:
        repository.handle(payload=payload)

    assert error.type == ValidationError
    assert error.value.status_code == 400


def test_update_payment_repository_success(loan, payment_with_loan):
    loan.id = uuid4()
    loan.save()

    payment_with_loan.loan = loan
    payment_with_loan.id = uuid4()
    payment_with_loan.save()

    payload = {"id": payment_with_loan.id, "is_paid": True}

    repository = UpdatePaymentRepository()
    response = repository.handle(payload=payload)

    assert response.is_paid is True
    assert response.id == payment_with_loan.id


def test_balance_payment_repository_error():
    repository = BalancePaymentRepository()
    loan_uuid = uuid4()

    with pytest.raises(ValidationError) as error:
        repository.handle(loan_uuid=loan_uuid)

    assert error.type == ValidationError
    assert error.value.status_code == 400


def test_balance_payment_repository_success(loan, payment_with_loan):
    loan.id = uuid4()
    loan.save()

    payment_with_loan.loan = loan
    payment_with_loan.id = uuid4()
    payment_with_loan.save()

    repository = BalancePaymentRepository()
    response = repository.handle(loan_uuid=loan.id)

    assert response[0].id == payment_with_loan.id


@patch("src.apps.payments.api.v1.repositories.CreatePaymentRepository.handle")
def test_create_payment_repository_operational_error(mock_repository, loan):
    repository = CreatePaymentRepository()

    mock_repository.side_effect = OperationalError()

    with pytest.raises(OperationalError) as error:
        repository.handle(
            loan=loan,
            installments_amount="500.00",
            installments=2,
        )

    assert isinstance(error.value, OperationalError)


@patch("src.apps.payments.api.v1.repositories.CreatePaymentRepository.handle")
def test_create_payment_repository_integrity_error(mock_repository, loan):
    repository = CreatePaymentRepository()

    mock_repository.side_effect = IntegrityError()

    with pytest.raises(IntegrityError) as error:
        repository.handle(
            loan=loan,
            installments_amount="500.00",
            installments=2,
        )

    assert isinstance(error.value, IntegrityError)


def test_create_payment_repository_success(loan):
    repository = CreatePaymentRepository()

    response = repository.handle(
        installments_amount=500.00,
        installments=2,
        loan=loan,
    )

    assert response is None
