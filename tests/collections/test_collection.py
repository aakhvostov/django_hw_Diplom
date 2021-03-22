import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from collection.models import Collection


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
    col_title = "best collection"
    col_text = "best of the best"
    response = api_client_staff.post(
        url,
        {
            "title": col_title,
            "text": col_text
        })
    assert response.status_code == HTTP_201_CREATED
    resp_json = response.json()
    assert resp_json.get("id")
    collection = Collection.objects.get(id=resp_json["id"])
    assert resp_json["title"] == collection.title
    assert resp_json["text"] == collection.text


@pytest.mark.django_db
def test_collection_detail(api_client, collection_factory, product_in_collection_factory):
    """ Вывод подборки на чтение"""

    collection = collection_factory()
    url = reverse("collections-detail", args=(collection.id,))
    products = product_in_collection_factory(_quantity=10, collection=collection)
    response = api_client[0].get(url)
    assert response.status_code == HTTP_200_OK
    #  ДОДЕЛАТЬ! вывод на показ всех продуктов в подборке!


@pytest.mark.django_db
def test_collection_delete(api_client_staff, collection_factory, product_in_collection_factory):
    """ Удаление подборки админом"""

    collection = collection_factory()
    url = reverse("collections-detail", args=(collection.id,))
    response = api_client_staff.delete(url)
    assert response.status_code == HTTP_204_NO_CONTENT
