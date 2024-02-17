from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignupForm

from django.http import HttpResponse



def hello_world(request):
    context = {'name':'Thabang Motswenyane'}
    return render(request, 'index.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
"""
does not want to work it does not redirect instead it refreshes only
"""
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def navigation(request):
    context = {'name':'Thabang Motswenyane'}
    return render(request, 'navigation_bar.html', context)