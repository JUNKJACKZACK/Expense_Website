import email
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from django.db import models
from flask import stream_template
from sqlalchemy import LABEL_STYLE_TABLENAME_PLUS_COL

# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length = 255)
    

class Product(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.DecimalField()


class Product(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True)
    collection = models.ForeignKey(Collection, on_delete = models.PROTECT)
    
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    phone = models.models.CharField(max_length = 255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length = 1, choices = MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE )
    
    
    class Order(models.Model):
        PAYMENT_STATUS_PENDING = 'P'
        PAYMENT_STATUS_COMPLETE = 'C'
        PAYMENT_STATUS_FAILED = 'F'
        PAYMENT_STATUS_CHOICES= [
            (PAYMENT_STATUS_PENDING, 'Pending'),
            (PAYMENT_STATUS_COMPLETE, 'Complete')
            (PAYMENT_STATUS_FAILED, 'Failed')
        ]
        
        
        placed_at = models.DateTimeField(auto_now_add = True)
        payment_status = models.CharField(
            max_length = 1, choices = PAYMENT_STATUS_CHOICES, default = PAYMENT_STATUS_PENDING)
        customer = models.ForeignKey(Customer, on_delete = models.PROTECT)
        

class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    customer = models.ForeignKey(
        Customer, on_delete = models.CASCADE)
    
    
class Test:
    print("login")
