from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(requests):
    return render(requests,'index.html')

def add_emp(requests):
    if requests.method == 'POST':
        first_name = requests.POST['first_name']
        last_name = requests.POST['last_name']
        phone = int(requests.POST['phone'])
        salary = int(requests.POST['salary'])
        bonus = int(requests.POST['bonus'])
        dept = int(requests.POST['dept'])
        role = int(requests.POST['role'])
        new_emp = Employee(first_name=first_name,last_name=last_name,phone=phone,dept_id=dept,role_id=role,salary=salary,bonus=bonus,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("New Employee Added Successfully")
    elif requests.method == 'GET':
        return render(requests, 'add_emp.html')
    else:
        return HttpResponse("An Error Occured! Employee not added.")



def all_emp(requests):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(requests,'view_all_emp.html',context)
def del_emp(requests,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")

        except:
            return HttpResponse("Enter a valid Employee Id")

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(requests,'del_emp.html',context)
def filter_emp(requests):
    if requests.method == 'POST':
        name = requests.POST['name']
        # phone = requests.POST['phone']
        dept = requests.POST['dept']
        role = requests.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        # if phone:
        #     emps = emps.filter(phone__icontains = phone)
        context = {
            'emps': emps
        }
        return render(requests,'view_all_emp.html',context)
    elif requests.method=='GET':
        return render(requests, 'filter_emp.html')
    else:
        return HttpResponse("An error ocuured!")





