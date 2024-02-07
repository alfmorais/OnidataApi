import pytest
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from tests._factories import UserFactory


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
