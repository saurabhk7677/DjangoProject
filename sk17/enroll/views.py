from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('form validated')
            print(fm.cleaned_data)
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
        print("ye get request he")

    return render(request, 'enroll/userregistration.html', {'form':fm})


    
