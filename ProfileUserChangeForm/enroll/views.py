from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpUser,EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# User Sign Up View.......
def user_signup(request):
    if request.method == 'POST':
        fm = SignUpUser(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Successfully Created !!!!!!!')
            fm.save()
    else:
        fm = SignUpUser()
    return render(request, 'enroll/signup.html', {'form': fm})


#User Login View.........
def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            user.save()
            if user is not None:
                login(request, user)
                messages.success(request, 'Loged In Successfully !!!!')
                return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request, 'enroll/login.html', {'form':  fm})



# User Profile view.......
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Profile Updated !!!')
                fm.save()
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request, 'enroll/profile.html', {'name':
        request.user, 'form': fm})
    else:
        return HttpResponseRedirect('/login/')


# User Logout View......
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')



# User Password Change.......
def user_changepass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Successfully Changed Password !!!!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')