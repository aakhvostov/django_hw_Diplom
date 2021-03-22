import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture
def user_staff_factory():

    def factory(**kwargs):
        return baker.make("User", is_staff=True, **kwargs)

    return factory


@pytest.fixture
def collection_factory():

    def factory(**kwargs):
        return baker.make("Collection", **kwargs)

    return factory


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
