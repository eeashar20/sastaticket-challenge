from rest_framework.routers import DefaultRouter

from store.views import CustomerViewSet, OrderViewSet, OrderItemViewSet, ProductViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet, basename='customers')
router.register('orders', OrderViewSet, basename='orders')
router.register('items', OrderItemViewSet, basename='items')
router.register('products', ProductViewSet, basename='items')

urlpatterns = router.urls
