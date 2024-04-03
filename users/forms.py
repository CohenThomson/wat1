from django import forms
from users.models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['firstname', 'surname', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput)
