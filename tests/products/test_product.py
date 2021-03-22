import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED


@pytest.mark.django_db
def test_product_list(api_client, product_factory):
    url = reverse("products-list")
    product_factory(_quantity=10)
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    resp_json = response.json()
    assert resp_json["name"]
    results = resp_json["name"]
    assert len(results) == 10


@pytest.mark.django_db
def test_product_create(api_client, product_factory):
    url = reverse("products-list")
    product = product_factory()
    response = api_client.post(url, product)
    assert response.status_code == HTTP_201_CREATED
    resp_json = response.json()
    assert resp_json["id"]
    assert resp_json["id"] == product.id
    assert resp_json["name"] == product.name
    assert resp_json["description"] == product.description
