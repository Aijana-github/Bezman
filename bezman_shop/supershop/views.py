from django.shortcuts import render
from .models import *

# Create your views here.

def productList(request):
    product = Product.object.all()
    return  render (request,'supershop/products.html')
