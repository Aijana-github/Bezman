from django.db import models
from accounts.models import Customer


# Create your models here.

class Product(models.Model):
    types = (
        ('classic','classic'),
        ('sport','sport'),
        ('dm','demi-season'),
        ('winter','winter')

    )
    genders = (
        ('male','male'),
        ('female','female'),
        ('uni','uni'),
    )
    sizes = (
        ('child','child'),
        ('medium','medium'),
        ('large','large'),
        ('XL','XL'),
    )
    name = models.CharField(max_length=40)
    product_type = models.CharField(max_length=40,choices=types)
    gender = models.CharField(max_length=20,choices=genders)
    product_model = models.CharField(max_length=50)
    price = models.IntegerField()
    size = models.CharField(max_length=20,choices=sizes)
    manufacturer = models.CharField(max_length=15)
    image = models.ImageField(blank=True,default='default.png')

    def __str__(self):
        return self.name+' '+self.product_model

class Order(models.Model):
    statuses = (
        ('Not Delivered','Not Delivered'),
        ('In process','In process'),
        ('Delivered','Delivered')
    )
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=statuses,default='Not Delivered')
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.product.name + ' '+ self.status