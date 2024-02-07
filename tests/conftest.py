from uuid import uuid4

import pytest
from pytest_factoryboy import register
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from tests._factories import LoansFactory, PaymentFactory, UserFactory
from tests._utils import response_body_replace

register(UserFactory, "user")
register(LoansFactory, "loan")
register(PaymentFactory, "payment")


@pytest.fixture
def user():
    return UserFactory(username="admin")


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def api_token(db, user):
    token, _ = Token.objects.get_or_create(user=user)
    return token


@pytest.fixture
def api_client_logged(db, api_client, api_token):
    api_client.credentials(HTTP_AUTHORIZATION="Token " + api_token.key)
    return api_client


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [
            ("X-VTEX-API-AppKey", "DUMMYID"),
            ("X-VTEX-API-AppToken", "DUMMYKEY"),
            ("authorization", "DUMMYBEARER"),
            ("Authorization", "DUMMYBEARER"),
        ],
        "filter_query_parameters": [
            ("apikey", "THIS_IS_NOT_A_APIKEY"),
            ("hapikey", "THIS_IS_NOT_A_APIKEY"),
            ("access_key", "THIS_IS_NOT_A_APIKEY"),
            ("key", "THIS_IS_NOT_A_APIKEY"),
        ],
        "filter_post_data_parameters": [
            (
                "AUTHORIZATION",
                {
                    "PASSWORD": "DummyPassWord",
                    "USERNAME": "DummyUsername",
                },
            ),
            ("password", "dummypass"),
            ("username", "dummyuser"),
        ],
        "before_record_response": response_body_replace(
            {
                "token": "valid_token",
                "access_token": "valid_token",
            },
        ),
    }


@pytest.fixture
def payment_with_loan():
    customer = UserFactory.create(username="Bruce Wayne")
    customer.save()

    loan = LoansFactory.create(
        id=uuid4(),
        customer=customer,
    )
    loan.save()

    payment = PaymentFactory.create(
        id=uuid4(),
        loan=loan,
    )
    payment.save()

    return payment
