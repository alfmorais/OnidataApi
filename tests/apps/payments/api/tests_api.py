from uuid import uuid4

import pytest

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    "status_code, payload, expected_response",
    [
        (400, {"is_paid": True}, {"id": ["This field is required."]}),
        (
            400,
            {"id": "3838f699-a7f3-4ccc-8cdd-ddbb56c68989"},
            {"is_paid": ["This field is required."]},
        ),
    ],
)
def test_update_payment_error(
    status_code,
    payload,
    expected_response,
    api_client_logged,
):
    url = "/v1/payments/"
    response = api_client_logged.put(url, payload, format="json")

    assert response.json() == expected_response
    assert response.status_code == status_code


def test_update_payment_not_authorized(api_client):
    url = "/v1/payments/"
    response = api_client.put(url, {}, format="json")

    expected_result = {
        "detail": "Authentication credentials were not provided.",
    }
    response_json = response.json()

    assert response.status_code == 401
    assert response_json == expected_result


def test_update_payment_success(api_client_logged, payment_with_loan):
    payload = {"id": payment_with_loan.id, "is_paid": True}

    url = "/v1/payments/"
    response = api_client_logged.put(url, payload, format="json")
    response_json = response.json()["data"]

    assert response_json["is_paid"] is True


def test_update_payment_not_found_error(api_client_logged):
    payment_uuid = uuid4()
    payload = {"id": payment_uuid, "is_paid": True}

    url = "/v1/payments/"
    response = api_client_logged.put(url, payload, format="json")
    expected_result = {"error": "Payment not found"}

    assert response.status_code == 400
    assert response.json() == expected_result


def test_list_all_payments_not_authorized(api_client, loan):
    loan.id = uuid4()
    loan.save()

    url = f"/v1/payments/{loan.id}/"
    response = api_client.get(url, format="json")

    expected_result = {
        "detail": "Authentication credentials were not provided.",
    }
    response_json = response.json()

    assert response.status_code == 401
    assert response_json == expected_result


def test_list_all_payments_not_found_error(api_client_logged):
    loan_uuid = uuid4()

    url = f"/v1/payments/{loan_uuid}/"
    response = api_client_logged.get(url, format="json")

    expected_result = {"error": "Payments not found"}
    response_json = response.json()

    assert response.status_code == 400
    assert response_json == expected_result


def test_list_all_payments_success(api_client_logged, loan, payment_with_loan):
    loan.id = uuid4()
    loan.save()

    payment_with_loan.loan = loan
    payment_with_loan.save()

    url = f"/v1/payments/{loan.id}/"
    response = api_client_logged.get(url, format="json")

    expected_result = [
        "date",
        "id",
        "installment_amount",
        "installment_number",
        "is_paid",
        "loan",
    ]
    response_json = response.json()["data"][0]

    assert response.status_code == 200
    assert sorted(response_json) == expected_result


def test_list_balance_by_loan_not_authorized(api_client, loan):
    loan.id = uuid4()
    loan.save()

    url = f"/v1/payments/{loan.id}/balance/"
    response = api_client.get(url, format="json")

    expected_result = {
        "detail": "Authentication credentials were not provided.",
    }
    response_json = response.json()

    assert response.status_code == 401
    assert response_json == expected_result


def test_list_balance_by_loan_not_found(api_client_logged):
    loan_uuid = uuid4()

    url = f"/v1/payments/{loan_uuid}/balance/"
    response = api_client_logged.get(url, format="json")

    expected_result = {"error": "Payments not found"}
    response_json = response.json()

    assert response.status_code == 400
    assert response_json == expected_result


def test_list_balance_by_loan_success(
    api_client_logged,
    loan,
    payment_with_loan,
):
    loan.id = uuid4()
    loan.save()

    payment_with_loan.loan = loan
    payment_with_loan.save()

    url = f"/v1/payments/{loan.id}/balance/"
    response = api_client_logged.get(url, format="json")

    expected_result = sorted(
        [
            "amount_missing_payment",
            "amount_paid",
            "installments_missing_payment",
            "installments_paid",
            "interest_rate",
            "loan_id",
            "total_installments",
        ]
    )
    response_json = response.json()["data"]

    assert response.status_code == 200
    assert sorted(response_json) == expected_result
