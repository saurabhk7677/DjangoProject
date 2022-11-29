from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showuserdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("form validated")
            print(fm.cleaned_data)
            fm = StudentRegistration()
            
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})