from django import forms
from .models import UserProfile
#creating the Login form



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }