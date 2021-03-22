import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK


@pytest.mark.django_db
def test_collection_list(api_client, collection_factory):
    url = reverse("product-collections")
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
