from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('products/',productList,name='products'),
    path('orders/',orderList,name='orders'),
    path('order-create/<int:product_id>/',orderCreate,name='order-create'),
    path('order-update/<int:order_id>/',orderUpdate,name='order-update'),
    path('task1/',task1),
    path('order-delete/<int:order_id>/',orderDelete,name='order-delete'),


]

