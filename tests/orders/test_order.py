import pytest
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK


@pytest.mark.django_db
def test_order_create(api_client, product_in_order_factory):
    url = reverse("orders-list")
    product_in_order = product_in_order_factory()
    order = product_in_order.order
    # Тут должна быть проверка на АДМИНА или
    response = api_client.post(url, order)
    assert response.status_code == HTTP_201_CREATED
    resp_json = response.json()
    assert resp_json["id"] == order.id
    assert resp_json["owner"] == order.owner
    assert resp_json["status"] == order.status


@pytest.mark.django_db
def test_order_list(api_client, order_factory):
    url = reverse("orders-list")
    order_factory(_quantity=4)
    # Тут должна быть проверка на АДМИНА или
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    resp_json = response.json()
    assert len(resp_json) == 4


@pytest.mark.django_db
def test_order_get(api_client, order_factory):
    order = order_factory()
    url = reverse("orders-detail", args=(order.id, ))
    # Тут должна быть проверка на АДМИНА или
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    resp_json = response.json()
    assert resp_json["id"] == order.id
    assert resp_json["owner"] == order.owner
    assert resp_json["status"] == order.status








