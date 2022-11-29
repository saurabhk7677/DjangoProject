from django import forms

class StudentUserdata(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter your Name'})
    email = forms.EmailField(error_messages={'required':'Enter your Email'})
    password = forms.CharField(error_messages={'required':'Enter your password'}, widget=forms.PasswordInput)
    rpassword = forms.CharField(error_messages={'required':'Enter your password'}, label='password(Re-Enter)', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpwd = self.cleaned_data['password']
        valrpwd = self.cleaned_data['rpassword']

        if valpwd != valrpwd:
            raise forms.ValidationError('password does not match')