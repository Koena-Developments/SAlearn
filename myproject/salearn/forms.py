from django import forms
from .models import UserProfile
#creating the Login form

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'my-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'my-input'}))

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'my-input'}),
            'email': forms.EmailInput(attrs={'class':'my-input'}),
            'password': forms.PasswordInput(attrs={'class':'my-input'}),
        }