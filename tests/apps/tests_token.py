import pytest

pytestmark = pytest.mark.django_db


def test_create_token_success(api_client, user):
    user.username = "alfredo@gmail.com"
    user.set_password("1234")
    user.save()

    url = "/api-token-auth/"
    payload = {"username": user.username, "password": "1234"}

    response = api_client.post(url, payload, format="json")

    assert response.status_code == 200
    assert sorted(response.json().keys())[0] == "token"


def test_create_token_fake_credentials_error(api_client):
    url = "/api-token-auth/"
    payload = {"username": "FakeUsername", "password": "FakePassword"}

    response = api_client.post(url, payload, format="json")

    assert response.status_code == 400
