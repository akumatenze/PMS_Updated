# serializers.py
from rest_framework import serializers
from .models import User

from django.db import models

class Customer(models.Model):
    cid = models.CharField(max_length=100, unique=True)  # Assuming cid is unique in Customer
    # Other fields in the Customer model

class Tenancy(models.Model):
    cid = models.CharField(max_length=100)  # Assuming cid is the same type as in Customer
    # Other fields in the Tenancy model
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Tenancy for Customer: {self.customer.cid}"

