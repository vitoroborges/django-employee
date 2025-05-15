from django.db import models

# Create your models here.

class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.CharField(50)
    city = models.CharField(50)
    state = models.CharField(50)

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(100)
    email = models.EmailField()
    phone = models.CharField(11)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=False)