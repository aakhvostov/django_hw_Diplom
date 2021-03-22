import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_review_list(api_client, review_factory):
    """ Получение списка отзывов на чтение"""

    url = reverse("reviews-list")
    review_factory(_quantity=4)
    response = api_client[0].get(url)
    assert response.status_code == HTTP_200_OK
    resp_json = response.json()
    assert len(resp_json) == 4


@pytest.mark.django_db
def test_review_create(api_client, product_factory):
    """ Создание отзыва"""

    url = reverse("reviews-list")
    product = product_factory()
    response = api_client[0].post(url, {
        "product": product.id,
        "text": "супер кружка",
        "rating": 5
    })
    assert response.status_code == HTTP_201_CREATED
    resp_json = response.json()
    assert resp_json["text"] == "супер кружка"
    assert resp_json["product"] == product.id


@pytest.mark.django_db
def test_review_get(api_client, review_factory):
    """ Получение отзыва владельцем"""

    client, user = api_client
    review = review_factory(author=user)
    url = reverse("reviews-detail", args=(review.id,))
    response = client.get(url)
    assert response.status_code == HTTP_200_OK
    resp_json = response.json()
    assert resp_json["id"] == review.id
    assert resp_json["text"] == review.text
    assert resp_json["rating"] == review.rating


@pytest.mark.django_db
def test_review_delete(api_client, review_factory):
    """ Удаление отзыва владельцем"""

    client, user = api_client
    review = review_factory(author=user)
    url = reverse("reviews-detail", args=(review.id,))
    response = client.delete(url)
    assert response.status_code == HTTP_204_NO_CONTENT
