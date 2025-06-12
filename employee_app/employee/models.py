from django.db import models
# Create your models here.

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    birth_date = models.DateField()
    function = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)