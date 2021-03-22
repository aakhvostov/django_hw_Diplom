import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_collection_list(api_client, collection_factory, product_in_collection_factory):
    """ Получение списка подборок на чтение"""

    url = reverse("collections-list")
    collection = collection_factory()
    products = product_in_collection_factory(_quantity=10, collection=collection)
    response = api_client[0].get(url)
    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_collection_create(api_client_staff, collection_factory, product_in_collection_factory):
    """ Создание подборки админом"""

    url = reverse("collections-list")
    response = api_client_staff.post(
        url,
        {
            "title": "test collection",
            "text": "super collection"
        })
    assert response.status_code == HTTP_201_CREATED
    resp_json = response.json()
    assert resp_json["title"] == "test collection"
    assert resp_json["text"] == "super collection"


@pytest.mark.django_db
def test_collection_list(api_client, collection_factory, product_in_collection_factory):
    """ Получение подбороки на чтение"""

    collection = collection_factory()
    url = reverse("collections-detail", args=(collection.id,))
    products = product_in_collection_factory(_quantity=10, collection=collection)
    response = api_client[0].get(url)
    assert response.status_code == HTTP_200_OK
    #  ДОДЕЛАТЬ! вывод на показ всех продуктов в подборке!


@pytest.mark.django_db
def test_collection_create(api_client_staff, collection_factory, product_in_collection_factory):
    """ Удаление подборки админом"""

    collection = collection_factory()
    url = reverse("collections-detail", args=(collection.id,))
    response = api_client_staff.delete(url)
    assert response.status_code == HTTP_204_NO_CONTENT
