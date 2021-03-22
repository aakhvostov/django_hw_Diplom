import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from rest_framework_simplejwt.tokens import RefreshToken


def factory_user_staff(**kwargs):
    return baker.make("User", is_staff=True, **kwargs)


def factory_user(**kwargs):
    return baker.make("User", **kwargs)


@pytest.fixture
def api_client():
    client = APIClient()
    user = factory_user()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Gluk {refresh.access_token}')
    return client, user


@pytest.fixture
def api_client_staff():
    client = APIClient()
    user = factory_user_staff()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Gluk {refresh.access_token}')
    return client


@pytest.fixture
def product_factory():

    def factory(**kwargs):
        return baker.make("Product", **kwargs)

    return factory


@pytest.fixture
def order_factory():

    def factory(**kwargs):
        return baker.make("Order", **kwargs)

    return factory


@pytest.fixture
def product_in_order_factory():

    def factory(**kwargs):
        return baker.make("ProductInOrder", **kwargs)

    return factory


@pytest.fixture
def review_factory():

    def factory(**kwargs):
        return baker.make("Review", **kwargs)

    return factory


@pytest.fixture
def collection_factory():

    def factory(**kwargs):
        return baker.make("Collection", **kwargs)

    return factory


@pytest.fixture
def product_in_collection_factory():

    def factory(**kwargs):
        return baker.make("ProductInCollection", **kwargs)

    return factory
