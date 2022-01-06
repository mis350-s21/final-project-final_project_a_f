from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField(max_length=12, null=False, unique=True)
    CName = models.CharField(max_length=50, null=False)
    date_of_birth = models.DateField(null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=8, null=False, unique=True)
    address = models.CharField(max_length=100, null=False)
    credit_card = models.CharField(max_length=16, null=True)


class Order(models.Model):
    order_id = models.CharField(max_length=12, null=False, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Review(models.Model):
    review_id = models.CharField(max_length=10, null=False, unique=True)
    comment = TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    
class Book(models.Model):
    title=models.CharField(max_length=100, null=False)
    discription= models.CharField(max_length=150, null=False)
    price= models.FloatField(max_length=10, null=False)
    inventory= models.CharField(max_length=50, null=False)
      
def __str__(self):
    return self.title

class Genre(models.Model):
    type=models.CharField(max_length=50, null=False)
    allbook = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
    )

def __str__(self):
    return self.type 