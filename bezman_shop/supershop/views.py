from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django_filters.filters import OrderingFilter
from .filters import ProductFilter
from .decorators import allowed_roles

# Create your views here.
@allowed_roles(allowed=['bezman'])
def productList(request):
    products = Product.objects.all()
    filter = ProductFilter(request.GET,queryset=products)
    products = filter.qs
    context = {'products': products,'filter':filter}
    return render (request, 'supershop/products.html', context)

@login_required()
def orderList(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    orders_delivered = Order.objects.filter(status='Delivered').count()

    context = {'orders': orders,'orders_count':orders_count}
    return render(request, 'supershop/order-List.html', context)

def orderCreate(request,product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Order.DoesNotExist:
        return HttpResponse('page not found 404')
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
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return HttpResponse('page not found 404')
    form = OrdersForm(instance=order)
    if request.method == 'POST':
        form = OrdersForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form':form}
    return render(request,'supershop/order-create.html',context)

def task1(request):
    ## solution
    string = "aaaaaaaaaaaab"
    i = set(string)
    if len(string) % 2 == 0:
        return HttpResponse(string)
    else:
        return HttpResponse('Chat with her')


def orderDelete(request,order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return HttpResponse('No such Order.')
    form = OrdersForm(instance=order)
    if request.method == 'POST':
        if order.status == 'Not Delivered':
            order.delete()
            return HttpResponse('Order Deleted!')
        else:
            return HttpResponse('Not Valid Status for delete order!')
    context = {'order':order}
    return render(request,'supershop/order-delete.html, context')






















