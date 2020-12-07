from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django_filters.filters import OrderingFilter
from .filters import ProductFilter

# Create your views here.

def productList(request):
    products = Product.objects.all()
    filter = ProductFilter(request.GET,queryset=products)
    products = filter.qs
    context = {'products': products,'filter':filter}
    return render (request, 'supershop/products.html', context)

def orderList(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    orders_delivered = Order.objects.filter(status='Delivered').count()

    context = {'orders': orders,'orders_count':orders_count}
    return render(request, 'supershop/order-List.html', context)

def orderCreate(request,product_id):
    product = Product.objects.get(id=product_id)
    customer = request.user
    form = OrdersForm(initial={'product':product,'customer':customer})

    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form':form}
    return  render(request,'supershop/order-create.html',context)


def orderUpdate(request,order_id):
    order = Order.objects.get(id=order_id)
    form = OrdersForm(instance=order)
    if request.method == 'POST':
        form = OrdersForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form':form}
    return render(request,'supershop/order-create.html',context)



