from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from tests.django_test_app.models import SampleModel
from tests.django_test_app.serializers import SampleSerializer


class SampleViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = SampleSerializer

    def get_queryset(self):
        return SampleModel.objects.all()
