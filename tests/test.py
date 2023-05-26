import pytest
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db

def test_samples(client):
    url = reverse(
        'books-list'
    )
    client.get(url).content
