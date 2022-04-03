from django import forms

class Inputform(forms.Form):
    user_name = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)