from django.shortcuts import render
from .models import Employee
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from rest_framework import viewsets, permissions
from .serializers import EmployeeSerializer

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


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
        Employee.objects.create(
            name=name,
            email=email,
            phone=phone,
            birth_date=birth_date,
            function=function,
            salary=salary
        )
        return HttpResponseRedirect('/employee/listEmployee')
    return render(request, 'employee_create.html')
    

@login_required(login_url='/employee/login')
def employee_update(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.phone = request.POST.get('phone')
        employee.birth_date = request.POST.get('birth_date')
        employee.function = request.POST.get('function')
        employee.salary = request.POST.get('salary')
        employee.save()
        return HttpResponseRedirect(reverse('employee_list'))
    return render(request, 'employee_update.html', {'employee': employee})

@login_required(login_url='/employee/login')
def employee_delete(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return HttpResponseRedirect('/employee/listEmployee')
