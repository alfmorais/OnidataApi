import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    "status_code, payload, expected_response",
    [
        (
            400,
            {
                "interest_rate": 1.1,
                "ip_address": "172.27.74.161",
                "bank": "Nu Pagamentos SA",
                "installments": 3,
                "insurance": 5.0,
            },
            {"amount": ["This field is required."]},
        ),
        (
            400,
            {
                "amount": 5000.00,
                "ip_address": "172.27.74.161",
                "bank": "Nu Pagamentos SA",
                "installments": 3,
                "insurance": 5.0,
            },
            {"interest_rate": ["This field is required."]},
        ),
        (
            400,
            {
                "amount": 5000.00,
                "interest_rate": 1.1,
                "bank": "Nu Pagamentos SA",
                "installments": 3,
                "insurance": 5.0,
            },
            {"ip_address": ["This field is required."]},
        ),
        (
            400,
            {
                "amount": 5000.00,
                "interest_rate": 1.1,
                "ip_address": "172.27.74.161",
                "installments": 3,
                "insurance": 5.0,
            },
            {"bank": ["This field is required."]},
        ),
        (
            400,
            {
                "amount": 5000.00,
                "interest_rate": 1.1,
                "ip_address": "172.27.74.161",
                "bank": "Nu Pagamentos SA",
                "insurance": 5.0,
            },
            {"installments": ["This field is required."]},
        ),
        (
            400,
            {
                "amount": 5000.00,
                "interest_rate": 1.1,
                "ip_address": "172.27.74.161",
                "bank": "Nu Pagamentos SA",
                "installments": 3,
            },
            {"insurance": ["This field is required."]},
        ),
    ],
)
def test_create_loan_error(
    status_code,
    payload,
    expected_response,
    api_client_logged,
):
    url = "/v1/loans/"
    response = api_client_logged.post(url, payload, format="json")

    assert response.json() == expected_response
    assert response.status_code == status_code


def test_create_loan_not_authorized(api_client):
    url = "/v1/loans/"
    response = api_client.post(url, format="json")

    expected_result = {
        "detail": "Authentication credentials were not provided.",
    }
    response_json = response.json()

    assert response.status_code == 401
    assert response_json == expected_result


def test_create_loan_success(api_client_logged):
    url = "/v1/loans/"
    payload = {
        "amount": 5000.00,
        "interest_rate": 1.1,
        "ip_address": "172.27.74.161",
        "bank": "Nu Pagamentos SA",
        "installments": 3,
        "insurance": 5.0,
    }
    response = api_client_logged.post(url, payload, format="json")
    response_json = response.json()["data"]
    expected_keys = [
        "amount",
        "bank",
        "cet_amount",
        "customer",
        "date",
        "id",
        "installments",
        "insurance",
        "interest_rate",
        "iof_interest_rate",
        "ip_address",
    ]

    assert response.status_code == 201
    assert sorted(response_json) == expected_keys


def test_list_all_loans_empty_success(api_client_logged):
    url = "/v1/loans/"
    response = api_client_logged.get(url, format="json")

    expected_result = {"data": []}
    response_json = response.json()

    assert response.status_code == 200
    assert response_json == expected_result


def test_list_all_loans_with_database_success(api_client_logged, loan):
    url = "/v1/loans/"
    response = api_client_logged.get(url, format="json")

    response_json = response.json()["data"][0]
    expected_keys = [
        "amount",
        "bank",
        "cet_amount",
        "customer",
        "date",
        "id",
        "installments",
        "insurance",
        "interest_rate",
        "iof_interest_rate",
        "ip_address",
    ]

    assert response.status_code == 200
    assert sorted(response_json) == expected_keys


def test_list_all_loans_not_authorized(api_client):
    url = "/v1/loans/"
    response = api_client.get(url, format="json")

    expected_result = {
        "detail": "Authentication credentials were not provided.",
    }
    response_json = response.json()

    assert response.status_code == 401
    assert response_json == expected_result
