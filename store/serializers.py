from rest_framework.serializers import ModelSerializer

from store.models import Customer, Product, Order, OrderItem


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'birth_date']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'unit_price']


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'payment_status', 'placed_at', 'items']


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'unit_price']
