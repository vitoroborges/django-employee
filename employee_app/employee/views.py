from django.shortcuts import render
from .models import Address, Employee
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def formlogin(request):

    if request.method == "POST":
        usuario = request.POST['login']
        senha = request.POST['senha']        
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/employee/listEmployee")
    
    return render(request, "login.html")

def logout_view(request):
    logout(request)

@login_required(login_url='/employee/login')
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

@login_required(login_url='/employee/login')
def employee_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address_id = request.POST.get('address_id')
        address = Address.objects.get(id=address_id)
        Employee.objects.create(name=name, email=email, address=address)
        return HttpResponseRedirect(reverse('employee_list'))
    addresses = Address.objects.all()
    return render(request, 'employee_create.html', {'addresses': addresses})

@login_required(login_url='/employee/login')
def employee_update(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        address_id = request.POST.get('address_id')
        employee.address = Address.objects.get(id=address_id)
        employee.save()
        return HttpResponseRedirect(reverse('employee_list'))
    addresses = Address.objects.all()
    return render(request, 'employee_update.html', {'employee': employee, 'addresses': addresses})

@login_required(login_url='/employee/login')
def employee_delete(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return HttpResponseRedirect(reverse('employee_list'))
    return render(request, 'employee_delete.html', {'employee': employee})

