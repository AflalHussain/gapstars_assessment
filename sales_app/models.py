# Create your models here.
# models.py in your app

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"Cart for {self.user.username}"


class CartItem(models.Model):
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart"

    def total_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderDetail')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
