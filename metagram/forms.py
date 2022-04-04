from django import forms

class Signupform(forms.Form):
    user_name = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    full_name = forms.CharField(label='full_name', max_length=100)
    
class Loginform(forms.Form):
    user_name = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)    
    
