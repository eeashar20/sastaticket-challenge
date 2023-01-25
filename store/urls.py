from rest_framework.routers import DefaultRouter

from store.views import CustomerViewSet, OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet, basename='customers')
router.register('orders', OrderViewSet, basename='orders')
router.register('items', OrderItemViewSet, basename='items')

urlpatterns = router.urls
