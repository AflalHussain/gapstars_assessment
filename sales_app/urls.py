from django.urls import path

from .views import CartView, CreateOrderView, DeleteFromCartView, ProductDetailsView, ProductsListView

urlpatterns = [
    path('products', ProductsListView.as_view(), name='product_list'),
    path('products/<int:product_id>', ProductDetailsView.as_view(), name='get_product_details'),
    path('cart', CartView.as_view()),
    path('cart/<int:product_id>', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('order', CreateOrderView.as_view()),
]
