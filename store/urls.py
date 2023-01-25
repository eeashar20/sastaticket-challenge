from django.urls import path
from rest_framework.routers import DefaultRouter

from store.views import CustomerViewSet, OrderViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet, basename='customers')
router.register('orders', OrderViewSet, basename='orders')

urlpatterns = router.urls
