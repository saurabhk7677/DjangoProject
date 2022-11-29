from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showuserdata(request):
    fm = StudentRegistration(auto_id=True)
    fm.order_fields(field_order=['email','password','name','contact'])
    return render(request, 'enroll/userregistration.html', {'form':fm})