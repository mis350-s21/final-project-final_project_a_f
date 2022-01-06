from django.db import models

# Create your models here.

class Customer(models.Model):
    CName = models.CharField(max_length=50, null=False)
    date_of_birth = models.DateField(null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=8, null=False, unique=True)
    address = models.CharField(max_length=100, null=False)
    credit_card = models.CharField(max_length=16, null=True)





class Book(models.Model):
    title=models.CharField(max_length=100, null=False)
    discription= models.CharField(max_length=150, null=False)
    price= models.FloatField(max_length=10, null=False)
    inventory= models.CharField(max_length=50, null=False)
      
def __str__(self):
    return self.title

class Genra(models.Model):
    type=models.CharField(max_length=50, null=False)
    allbook = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
    )

def __str__(self):
    return self.type 