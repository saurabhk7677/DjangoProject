from django import forms

class StudentRegitration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()