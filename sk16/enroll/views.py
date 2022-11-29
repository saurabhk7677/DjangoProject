from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showuserdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('form validated')
            print(fm.cleaned_data)
            print('ye POST request se aaya he')
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
        print('ye get request se aaya he')
    return render(request, 'enroll/userregistration.html', {'form':fm})