import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db()
def test_samples(client):
    url = reverse(
        'SampleViewSet-list'
    )
    client.get(url).content
