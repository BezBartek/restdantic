from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from tests.django_test_app.models import Book
from tests.django_test_app.serializers import BookSerializer


class BookViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()
