from django import forms



class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={'default':'Enter your Name'})
    email = forms.EmailField(error_messages={'default':'Enter your Email'})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'default':'Enter your password'})