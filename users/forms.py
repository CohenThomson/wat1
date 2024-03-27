from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    user = forms.CharField(label='User', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    firstname = forms.CharField(label='First Name', max_length=30)
    surname = forms.CharField(label='Surname', max_length=150)
    email = forms.EmailField(label='Email')
    
    
    
    # user = forms.OneToOneField(label='user', User, on_delete=forms.CASCADE)
    # firstname = forms.CharField(label='firstname', max_length=50, null=True, blank=True)
    # surname = forms.CharField(label='surname', max_length=50, null=True, blank=True)
    # email = forms.EmailField(label='email', null=True, blank=True)
