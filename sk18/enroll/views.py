from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

# Create your views here.
def thankyou(request):
    return render(request, 'enroll/success.html')

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("form validated")
            print(fm.cleaned_data)
            return HttpResponseRedirect('/regi/success/')
            #return render(request, 'enroll/success.html', {'nm': name})
    else:
        fm = StudentRegistration()
        print("ye GET request he")

    return render(request, 'enroll/userregistration.html', {'form':fm})