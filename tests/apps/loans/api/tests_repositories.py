from unittest.mock import patch

import pytest
from django.db.utils import IntegrityError, OperationalError
from src.apps.loans.api.v1.repositories import (
    CreateLoanRepository,
    GetCustomerFromUserModelRepository,
    ListAllLoansRepository,
    LoansBaseRepository,
)

pytestmark = pytest.mark.django_db


def test_loans_base_respository_success(loan):
    repository = LoansBaseRepository()

    assert isinstance(loan, repository.model)


def test_list_all_loans_repository_success(loan, user):
    loan.customer = user
    loan.save()

    repository = ListAllLoansRepository()
    response = repository.handle(user_id=user.id)

    assert response[0].customer == user
    assert response[0].bank == loan.bank


def test_get_customer_from_user_model_repository_success(user):
    repository = GetCustomerFromUserModelRepository()
    response = repository.handle(user_id=user.id)

    assert response.id == user.id
    assert response.username == user.username


def test_create_loan_repository_success(loan, user):
    validated_data = {
        "amount": 5000.00,
        "interest_rate": "1.1",
        "ip_address": "172.27.74.161",
        "bank": "Nu Pagamentos SA",
        "installments": 3,
        "insurance": 5.0,
    }

    repository = CreateLoanRepository()
    response = repository.handle(
        user_id=user.id,
        validated_data=validated_data,
        iof_interest_rate=5.0,
        cet_amount=5500.00,
    )

    assert response.customer == user


@patch("src.apps.loans.api.v1.repositories.CreateLoanRepository.handle")
def test_create_loan_repository_integrity_error(mock_repository, user):
    mock_repository.side_effect = IntegrityError()

    validated_data = {
        "amount": 5000.00,
        "interest_rate": "1.1",
        "ip_address": "172.27.74.161",
        "bank": "Nu Pagamentos SA",
        "installments": 3,
        "insurance": 5.0,
    }

    repository = CreateLoanRepository()

    with pytest.raises(IntegrityError) as error:
        repository.handle(
            user_id=user.id,
            validated_data=validated_data,
            iof_interest_rate=5.0,
            cet_amount=5500.00,
        )

    assert isinstance(error.value, IntegrityError)


@patch("src.apps.loans.api.v1.repositories.CreateLoanRepository.handle")
def test_create_loan_repository_operational_error(mock_repository, user):
    mock_repository.side_effect = OperationalError()

    validated_data = {
        "amount": 5000.00,
        "interest_rate": "1.1",
        "ip_address": "172.27.74.161",
        "bank": "Nu Pagamentos SA",
        "installments": 3,
        "insurance": 5.0,
    }

    repository = CreateLoanRepository()

    with pytest.raises(OperationalError) as error:
        repository.handle(
            user_id=user.id,
            validated_data=validated_data,
            iof_interest_rate=5.0,
            cet_amount=5500.00,
        )

    assert isinstance(error.value, OperationalError)
