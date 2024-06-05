from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    billing_address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=[('P', 'Pending'), ('C', 'Completed'), ('F', 'Failed')])

class OrderLine(models.Model):
    order = models.ForeignKey(Order, related_name='order_lines', on_delete=models.CASCADE)
    product_id = models.IntegerField()  # Assuming product ID is an integer
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)