import pytest
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from order.models import Order


@pytest.mark.django_db
def test_order_create(api_client, order_factory, product_in_order_factory):
    """ Создание заказа авторизованным пользователем """
    client, user = api_client
    url = reverse("orders-list")
    response = client.post(url)
    assert response.status_code == HTTP_201_CREATED
    resp_json = response.json()
    assert resp_json.get("id")
    order = Order.objects.get(id=resp_json["id"])
    assert resp_json.get("owner")
    assert resp_json["owner"]["id"] == order.owner.id
    assert resp_json.get("status")
    assert resp_json.get("total_price")


@pytest.mark.django_db
def test_order_list(api_client_staff, order_factory):
    """ Получение списка заказов на чтение админом"""

    url = reverse("orders-list")
    count_orders = 6
    order_factory(_quantity=count_orders)
    response = api_client_staff.get(url)
    assert response.status_code == HTTP_200_OK
    resp_json = response.json()
    assert len(resp_json) == count_orders


@pytest.mark.django_db
def test_order_get(api_client, order_factory):
    """ Получение заказа владельцем"""

    client, user = api_client
    order = order_factory(owner=user)
    url = reverse("orders-detail", args=(order.id, ))
    response = client.get(url)
    assert response.status_code == HTTP_200_OK
    resp_json = response.json()
    assert resp_json["id"] == order.id
    assert resp_json["owner"]["id"] == order.owner.id
    assert resp_json["status"] == order.status


@pytest.mark.django_db
def test_order_status_change(api_client_staff, order_factory):
    """ Изменение статуса заказа админом"""

    order = order_factory()
    new_order_status = "IN_PROGRESS"
    url = reverse("orders-detail", args=(order.id, ))
    response = api_client_staff.patch(url, {"status": new_order_status})
    assert response.status_code == HTTP_200_OK
    resp_json = response.json()
    assert resp_json["id"] == order.id
    assert resp_json["status"] == new_order_status










