from rest_framework.viewsets import ModelViewSet

from store.models import Customer, Order, OrderItem
from store.serializers import CustomerSerializer, OrderSerializer, OrderItemSerializer


# Create your views here.

class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        authenticated_user = self.request.user.id
        return Customer.objects.filter(user_id=authenticated_user)


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        authenticated_user = self.request.user.id
        return Order.objects.filter(customer__user_id=authenticated_user)


class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        authenticated_user = self.request.user.id
        return OrderItem.objects.filter(order__customer__user_id=authenticated_user)
