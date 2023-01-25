from django.urls import path
from rest_framework.routers import DefaultRouter

from store.views import CustomerViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet, basename='customers')

urlpatterns = router.urls
