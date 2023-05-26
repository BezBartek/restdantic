from rest_framework import routers

from tests.django_test_app.api import BookViewSet

router = routers.SimpleRouter()

router.register(r'samples', BookViewSet, 'books')

urlpatterns = router.urls