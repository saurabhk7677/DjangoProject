from django.shortcuts import render
from .forms import StudentUserdata

# Create your views here.
def showuserdata(request):
    if request.method == 'POST':
        fm = StudentUserdata(request.POST)
        if fm.is_valid():
            print("form validated")
            print(fm.cleaned_data)
            fm = StudentUserdata()
    else:
        fm = StudentUserdata()
    return render(request, 'enroll/userregistration.html',{'form':fm})