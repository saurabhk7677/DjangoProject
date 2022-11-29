from django.shortcuts import render
from .models import Employee
from .forms import EmployeeDetails

# Create your views here.
def empinfo(request):
    emp_data = Employee.objects.all()
    return render(request, 'employee/empinfo.html', {'emp': emp_data})


def empdtails(request):
    if request.method == 'POST':
        emp_dtail = EmployeeDetails(request.POST)
        if emp_dtail.is_valid():
            print(emp_dtail.cleaned_data)
            emp_dtail.save()
    else:
        emp_dtail = EmployeeDetails()
    return render(request, 'employee/empdtail.html',{'empd': emp_dtail})
