from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse



def hello_world(request):
    context = {'name':'Thabang Motswenyane'}
    return render(request, 'index.html', context)
    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Handle successful login (e.g., redirect to dashboard)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def navigation(request):
    context = {'name':'Thabang Motswenyane'}
    return render(request, 'navigation_bar.html', context)