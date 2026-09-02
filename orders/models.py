from django.db import models
from products.models import Product

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(default=0)
    status = models.CharField(max_length=20, default='Pending')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items',null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
