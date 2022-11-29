from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# signup view function........
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
    return render(request, 'enroll/signup.html', {'form':fm})
    

# login view function.........
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully !!!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')


# profile view function......
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/login/')


# logout view function.....
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

