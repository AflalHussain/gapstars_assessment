from django.contrib import admin

from sales_app.models import Product, CartItem

# Register your models here.
admin.site.register(Product)
admin.site.register(CartItem)
