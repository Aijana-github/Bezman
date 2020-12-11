from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render,redirect
from .models import *
from .models import *
from .admin_only import admin_only



# Create your views here.

@admin_only
def customerList(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'accounts/customer_list.html', context)


def customerDetail(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = customer.order_set.all()
    context = {'customer':customer,'orders':orders}
    return render(request,'accounts/customer_detail.html',context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
             user = form.save()
             group = Group.objects.get(name='bezgirl')
             user.groups.add(group)
             Customer.objects.create(user=user,phone=1,full_name=user.username)
             user.save()
             return redirect('/')
    context = {'form':form}
    return render(request,'accounts/user_create.html',context)

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('products')
    context = {}
    return render(request,'accounts/login.html',context)

def logout_page(request):
    logout(request)
    return redirect('login')


