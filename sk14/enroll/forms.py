from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()                                       #(widget=forms.CheckboxInput)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)         #(widget=forms.FileInput) 
    contact = forms.IntegerField()                                 #(widget=forms.Textarea)
