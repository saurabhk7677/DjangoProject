from django.shortcuts import render, redirect
from employee.forms import EmployeeForm, OldNameForm, EmailForm
from employee.models import Employee,Oldname
from django.core.mail import send_mail
import smtplib
from crudexample import settings  
from django.http import HttpResponse  
from django.db import transaction

# Create your views here.
def send_email_form(request):
    context ={}
    context['form']= EmailForm()
    return render(request, "email.html", context)

# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass

    else:
        form = EmployeeForm()
    return render(request, 'index.html',{'form':form})

def show(request):
    employees = Employee.objects.filter(is_active= 1).select_related()
    return render(request,'show.html',{'employees':employees})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})

@transaction.atomic
def update(request, id):

    employee = Employee.objects.get(id=id)
    old_name = employee.ename
    form = EmployeeForm(request.POST,instance = employee)

    if form.is_valid():
        form.save()
        obj = Oldname(emp=employee, old_name=old_name)
        obj.save()
        return redirect("/show")
    return render(request, 'edit.html',{'employee':employee})

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    #employee.delete()
    employee.is_active= 0
    employee.save()
    return redirect("/show")

# def my_email(request):
#     send_mail(
#     'sent by python',
#     'sucessfully sent by python.....!',
#     'saurabhkadam1105@gmail.com',
#     ['diganbar@binaryhat.co', 'shubhambhoj75@gmail.com'],
#     fail_silently=False,
# )
#     return redirect("/show")


def send_email(request,id):
    print("call  function")
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')

    if subject and message and from_email:
       res = send_mail(subject, message, settings.EMAIL_HOST_USER, [from_email])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)  

def oldname(request,id):
    x = Oldname.objects.filter(emp=id)
    return render(request, 'show_old_name.html',{'x':x})
   
# def oldemail(request,id):
#     y = Oldemail.objects.filter(emp=id)
#     return HttpResponse(y)



    