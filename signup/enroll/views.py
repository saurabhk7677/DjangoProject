from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
            messages.success(request, 'Account Successfully Created !!!')
            fm.save()
            fm = SignUpForm()
    else:
        fm = SignUpForm()
        print("denied")
    return render(request, 'enroll/signup.html', {'form': fm})