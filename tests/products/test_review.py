import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED


@pytest.mark.django_db
def test_review_list(api_client, review_factory):
    url = reverse("reviews-list")
    review_factory(_quantity=4)
    # Тут должна быть проверка на АДМИНА или
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    resp_json = response.json()
    assert len(resp_json) == 4


@pytest.mark.django_db
def test_review_get(api_client, review_factory):
    review = review_factory()
    url = reverse("reviews-detail", args=(review.id, ))
    # Тут должна быть проверка на АДМИНА или
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    resp_json = response.json()
    assert resp_json["id"] == review.id
    assert resp_json["owner"] == review.owner
    assert resp_json["status"] == review.status


@pytest.mark.django_db
def test_review_create(api_client, user_staff_factory, review_factory):
    url = reverse("reviews-list")
    user_staff = user_staff_factory()
    reviews = review_factory({
        "author": user_staff
    })
    response = api_client.post(url, reviews)
    assert response.status_code == HTTP_201_CREATED
    resp_json = response.json()
    assert resp_json["id"] == reviews.id
    assert resp_json["author"] == reviews.author
    assert resp_json["text"] == reviews.text
    assert resp_json["rating"] == reviews.rating
