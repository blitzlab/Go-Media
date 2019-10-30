from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget = forms.PasswordInput(), label='Confirm Password')
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password1')
