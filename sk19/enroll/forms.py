from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(min_length=5, max_length=50, strip=False, error_messages={'required': 'Enter Your Name'})
    age = forms.IntegerField(min_value=18, max_value=65)
    price = forms.DecimalField(min_value=5, max_value=50, max_digits=4, decimal_places=1)
    rate = forms.FloatField(min_value=5, max_value=50)
    comment = forms.SlugField()
    email = forms.EmailField(min_length=5, max_length=50)
    website = forms.URLField(min_length=5, max_length=50)
    password = forms.CharField(min_length=5,max_length=50,widget=forms.PasswordInput)
    description = forms.CharField(widget=forms.Textarea)
    feedback = forms.CharField(min_length=5, max_length=50, widget=forms.TextInput(attrs={'class':'somecss1 somecss2', 'id':'uniqueid'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))
    agree = forms.BooleanField(label='I Agree')
