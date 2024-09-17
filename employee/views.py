from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm, UpdateEmployeeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.admin import User

# @login_required
def home(request):
    employees = Employee.objects.all()
    return render(request, 'employees/home.html', {'employees': employees})

# @login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

# @login_required
def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = UpdateEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UpdateEmployeeForm(instance=employee)
    return render(request, 'employees/update_employee.html', {'form': form, 'employee': employee})

# @login_required
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')
    return render(request, 'employees/delete_employee.html', {'employee': employee})
    
# @login_required
def employee_profile(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employees/profile.html', {'employee': employee})
