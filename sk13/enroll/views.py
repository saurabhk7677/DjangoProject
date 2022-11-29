from django.shortcuts import render
from .forms import StudentRegitration 
# Create your views here.
def showformdata(request):
    fm = StudentRegitration()
    return render(request, 'enroll/userregistration.html', {'form':fm})