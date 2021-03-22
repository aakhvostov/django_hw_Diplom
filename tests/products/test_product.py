import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED


@pytest.mark.django_db
def test_product_list(api_client, product_factory):
    url = reverse("products-list")
    product_factory(_quantity=2)
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    resp_json = response.json()
    assert len(resp_json) == 2


@pytest.mark.django_db
def test_product_create(api_client_staff):
    product_url = reverse("products-list")
    response = api_client_staff.post(product_url, {
        "name": "product[0].name",
        "description": "product[0].description",
        "price": 1234.21
    })
    assert response.status_code == HTTP_201_CREATED
    resp_json = response.json()
    assert resp_json["name"] == "product[0].name"
    assert resp_json["description"] == "product[0].description"
    assert resp_json["id"] == 1
