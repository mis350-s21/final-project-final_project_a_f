from django.db import models

# Create your models here.

class Customer(models.Model):
    CName = models.CharField(max_length=50, null=False)
    date_of_birth = models.DateField(null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=8, null=False, unique=True)
    address = models.CharField(max_length=100, null=False)
    credit_card = models.CharField(max_length=16, null=True)