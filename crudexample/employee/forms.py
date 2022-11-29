from django import forms
from employee.models import Employee, Oldname

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['eid', 'ename', 'eemail', 'econtact']

class OldNameForm(forms.ModelForm):
    class Meta:
        model = Oldname
        fields = ['old_name']

# creating a form
class EmailForm(forms.Form):
    subject = forms.CharField()
    message = forms.CharField()
    from_email = forms.CharField()
    