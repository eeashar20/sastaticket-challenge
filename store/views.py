from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
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

    def _get_orders_response(self, orders):
        order_serializer = OrderSerializer(orders, many=True)
        return Response(order_serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes=[IsAdminUser], url_name='get_user_orders',
            url_path='by-email')
    def get_orders_by_customer_email(self, request):
        emails = request.data.get('emails')

        if emails:
            orders = Order.objects.filter(customer__user__email__in=emails)
            if orders:
                return self._get_orders_response(orders)

            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        authenticated_user = self.request.user.id
        return OrderItem.objects.filter(order__customer__user_id=authenticated_user)
