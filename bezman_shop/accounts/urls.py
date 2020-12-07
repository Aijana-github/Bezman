from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('customers/',customerList),
    path('customers/<int:customer_id>/',customerDetail),
    path('register/',registration),
    path('login/',auth,name='login'),
    path('logout/',logout_page,name='logout'),


]
