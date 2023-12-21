from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from sales_app.models import Product, CartItem, Order, OrderDetail
from sales_app.serializers import ProductSerializer, CartItemSerializer, OrderSerializer


class ProductsListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class DeleteFromCartView(APIView):
    def delete(self, request, cart_item_id):
        cart_item = get_object_or_404(CartItem, pk=cart_item_id)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartView(APIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def post(self, request):
        product_id = request.data.get('product')
        product = get_object_or_404(Product, pk=product_id)
        # Addd product to cart if it does not exist already
        cart_item, created = CartItem.objects.get_or_create(product=product)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
        serializer = self.serializer_class(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        cart_items = CartItem.objects.all()
        serializer_class = CartItemSerializer(cart_items, many=True)
        return Response(serializer_class.data)


class CreateOrderView(APIView):

    def post(self, request):
        cart_items = CartItem.objects.all()

        if not cart_items.exists():
            return Response({"message": "Your cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        # Get delivery_date and delivery_time from the request data
        delivery_date = request.data.get('delivery_date')
        delivery_time = request.data.get('delivery_time')

        # Calculate total amount
        total_amount = sum(item.product.price * item.quantity for item in cart_items)

        # Create an order with delivery_date and delivery_time
        order = Order.objects.create(
            total_amount=total_amount,
            delivery_date=delivery_date,
            delivery_time=delivery_time
        )

        # Create order details
        for cart_item in cart_items:
            OrderDetail.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                subtotal=cart_item.product.price * cart_item.quantity
            )

        # Clear the cart
        cart_items.delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
