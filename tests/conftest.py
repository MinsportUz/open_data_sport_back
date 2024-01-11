import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def api_client_with_credentials():
    client = APIClient()
    client.login(username='admin', password='admin')
    return client


@pytest.fixture
def api_client_with_token():
    client = APIClient()
    response = client.post('/admin/login/', data={'username': 'admin', 'password': 'admin'})
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])
    return client