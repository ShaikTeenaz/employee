
from urllib import request
from django.shortcuts import redirect, render

from salary.forms import EmployeeForm
from salary.models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required
def home(request):
    employee=Employee.objects.all()
    return render(request,'salary/home.html',{'employees':employee})

def detail(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'salary/employee.html',{'employee':employee})
def add_employee(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_success')

    else:
        form=EmployeeForm()
    return render(request,'salary/add_employee.html',{'form':form})
def success_view(request):
    return render(request,'salary/success.html')

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form=UserCreationForm()
    return render(request,'salary/register.html',{'form':form})