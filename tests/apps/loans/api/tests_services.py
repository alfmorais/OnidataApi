import pytest
from freezegun import freeze_time
from src.apps.loans.api.v1.services import (
    DAILY_AMORTIZATION_VALUE,
    LIMIT_TAX_IOF_VALUE,
    TAX_TAXATION_VALUE,
    CetAmountService,
    CreateLoanService,
    IOFInterestRateService,
    ListAllLoansService,
    LoanTimeInDays,
)
from tests._factories import LoansFactory, UserFactory

pytestmark = pytest.mark.django_db


def test_tax_taxation_value_success():
    assert TAX_TAXATION_VALUE == 0.38


def test_daily_amortization_value_success():
    assert DAILY_AMORTIZATION_VALUE == 0.0082


def test_limit_tax_iof_value_success():
    assert LIMIT_TAX_IOF_VALUE == 0.03


@freeze_time("2024-02-06")
def test_loan_time_in_days_success():
    days = LoanTimeInDays.handle(installments=1)

    assert days == 29


def test_iof_interest_rate_service_limit_success():
    iof_value = IOFInterestRateService.handle(
        amount=10_000,
        loan_time_in_days=562,
    )

    assert iof_value == 338.00


def test_iof_interest_rate_service_not_reached_limit_success():
    iof_value = IOFInterestRateService.handle(
        amount=10_000,
        loan_time_in_days=15,
    )

    assert iof_value == 50.3


def test_cet_amount_service_success():
    iof_value = IOFInterestRateService.handle(
        amount=10_000,
        loan_time_in_days=15,
    )
    cet_amount = CetAmountService.handle(
        amount=10_000,
        interest_rate=5.0,
        installments=3,
        iof_interest_rate=iof_value,
        insurance=5,
    )

    assert cet_amount == "12207.88"
    assert isinstance(cet_amount, str)


pytest.mark.db


def test_list_all_loan_service_empty_success():
    user = UserFactory(username="us", password="pw")

    service = ListAllLoansService()
    response = service.handle(user_id=user.id)

    assert response.count() == 0


def test_list_all_loan_service_with_data_success():
    user = UserFactory(username="us", password="pw")
    loan = LoansFactory()
    loan.customer = user
    loan.save()

    service = ListAllLoansService()
    response = service.handle(user_id=user.id)

    assert response.count() == 1


def test_create_loan_service_success():
    user = UserFactory(username="us", password="pw")
    payload = {
        "amount": 5000.00,
        "interest_rate": "1.1",
        "ip_address": "172.27.74.161",
        "bank": "Nu Pagamentos SA",
        "installments": 3,
        "insurance": 5.0,
    }

    service = CreateLoanService()
    response = service.handle(user_id=user.id, validated_data=payload)

    assert response.customer == user
