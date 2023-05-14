from rest_framework import routers

from tests.django_test_app.api import SampleViewSet

router = routers.SimpleRouter()

router.register(r'samples', SampleViewSet, 'SampleViewSet')

urlpatterns = router.urls