import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from decimal import Decimal
from product.models import Product


@pytest.mark.django_db
def test_product_list(api_client, product_factory):
    """ Получение списка продуктов пользователем для чтения """

    url = reverse("products-list")
    product_factory(_quantity=2)
    response = api_client[0].get(url)
    assert response.status_code == HTTP_200_OK
    resp_json = response.json()
    assert len(resp_json) == 2


@pytest.mark.django_db
def test_product_create(api_client_staff):
    """ Создание продукта админом """

    product_url = reverse("products-list")
    product_name = "Pokemon"
    product_description = "Pikachu"
    product_price = 300.00
    response = api_client_staff.post(
        product_url,
        {
            "name": product_name,
            "description": product_description,
            "price": product_price
        })
    assert response.status_code == HTTP_201_CREATED
    resp_json = response.json()
    assert resp_json.get("id")
    product = Product.objects.get(id=resp_json["id"])
    assert resp_json["id"] == product.id
    assert resp_json["name"] == product.name
    assert resp_json["description"] == product.description
    assert Decimal(resp_json["price"]) == product.price
