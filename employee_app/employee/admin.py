from django.contrib import admin
from .models import Employee, Address

# Register your models here.
admin.site.register(Employee)
admin.site.register(Address)