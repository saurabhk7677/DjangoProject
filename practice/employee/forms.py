from django.core import validators
from django import forms
from . models import Employee


class EmployeeDetails(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'city', 'company', 'salary', 'bank']
