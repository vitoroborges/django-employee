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
        phone = request.POST.get('phone')
        birth_date = request.POST.get('birth_date')
        function = request.POST.get('function')
        salary = request.POST.get('salary')
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
        employee.phone = request.POST.get('phone')
        employee.birth_date = request.POST.get('birth_date')
        employee.function = request.POST.get('function')
        employee.salary = request.POST.get('salary')
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

def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'address_list.html', {'addresses': addresses})

def address_create(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        number = request.POST.get('number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        Address.objects.create(address=address, number=number, city=city, state=state)
        return HttpResponseRedirect(reverse('address_list'))
    return render(request, 'address_create.html')

def address_update(request, pk):
    address = Address.objects.get(id=pk)
    if request.method == 'POST':
        address.address = request.POST.get('address')
        address.number = request.POST.get('number')
        address.city = request.POST.get('city')
        address.state = request.POST.get('state')
        address.save()
        return HttpResponseRedirect(reverse('address_list'))
    return render(request, 'address_update.html', {'address': address})

def address_delete(request, pk):
    address = Address.objects.get(id=pk)
    if request.method == 'POST':
        address.delete()
        return HttpResponseRedirect(reverse('address_list'))
    return render(request, 'address_delete.html', {'address': address})
