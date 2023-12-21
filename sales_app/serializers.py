from rest_framework import serializers

from .models import Product, CartItem, OrderDetail, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'manufacturer', 'price', 'stock_quantity')


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity')


class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderDetail
        fields = ['product', 'quantity', 'subtotal']


class OrderSerializer(serializers.ModelSerializer):
    order_details = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'total_amount', 'delivery_date', 'delivery_time', 'created_at', 'order_details']
