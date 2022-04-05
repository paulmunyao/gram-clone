from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Loginform(forms.Form):
    user_name = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)
